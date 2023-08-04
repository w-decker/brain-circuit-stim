################################################
######## Module for Neuronal Simulation ########
################################################

# imports
import numpy as np
import matplotlib.pyplot as plt

# simulate circuit
def simCircuit(I):
    """Simulating a 1000 neuron circuit.
    Inputs: 
    I (np.array) -- stimulation time
    """
    # variables
    Ne = 800 # excitatory neurons
    Ni = 200 # inhibitory neurons
    re = np.random.rand(Ne)
    ri = np.random.rand(Ni) # random int
    a = np.hstack((0.02*np.ones(Ne), 0.02 + 0.08*ri))   
    b = np.hstack((0.2 * np.ones(Ne), 0.25 - 0.05 *ri))
    c = np.hstack((-65 + 15 * re**2, -65 * np.ones(Ni)))
    d = np.hstack((8 - 6 * re**2, 2 * np.ones(Ni)))
    v = -65*np.ones(Ne + Ni)
    u = b*v
    firings = np.array([[],[]])
    S = np.hstack((0.5*np.random.rand(Ne + Ni, Ne), - np.random.rand(Ne + Ni, Ni)))

    for i in range(len(I)):
        # define I
        stim = np.hstack((4*np.random.randn(Ne), 1*np.random.randn(Ni))) + I[i]
        # check for activity (action potentials)
        fired = np.where(v >= 30)[0] # gives list of indices where v >= 30
        # spike indices and times
        X = np.stack((np.tile(i, len(fired)), fired))
        firings = np.concatenate((firings, X), axis=1)
        # update membrane vars with spikes
        v[fired] = c[fired]
        u[fired] += d[fired]
        # update I with spiking activity
        stim += np.sum(S[:, fired], axis=1)
        #update membrane potential
        v += .04*v**2 + 5*v + 140 - u + stim
        u += a*(b*v - u)

    return firings

def plotPopActivity(firings, I):
    """Plotting population level activity"""
    # initialize
    Ne = 800 # excitatory neurons
    Ni = 200 # inhibitory neurons
    time = int(np.max(firings[0,:]) + 1)
    pop_activity = np.zeros(time)

    # get average porportion of neurons firing at each time point
    for i in range(time):
        pop_activity[i] = np.sum(firings[0,:]==i)/(Ne + Ni)

    # spectral analysis
    pop_spectral = np.abs(np.fft.fft(pop_activity-np.mean(pop_activity)))**2 # mean centering!
    hz = np.linspace(0, 1000/2, int(time/2+1)) # get frequencies


    fig, ax = plt.subplots(1, 3, figsize=(20, 5))
    fig.suptitle("Neuronal Circuitry")

    ax[0].plot(firings[0,:],firings[1,:],'k.',markersize=1)
    ax[0].plot(I*50+100,'m',linewidth=2)
    ax[0].set_xlabel('Time (ms)')
    ax[0].set_ylabel('Neuron #')
    ax[0].set_title('Population spiking')

    ax[1].plot(pop_activity)
    ax[1].set_xlabel('Time (ms)')
    ax[1].set_ylabel('Porpotion of active neurons')
    ax[1].set_title('Porpotional Activity')

    ax[2].plot(hz, pop_spectral[:len(hz)]) # plot only positive
    ax[2].set_xlabel('Frequency (hz)')
    ax[2].set_ylabel('Spectral power')
    ax[2].set_xlim([0, 60])
    ax[2].set_title('Spectral activity')

    plt.show()