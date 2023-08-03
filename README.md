# brain-circuit-stim

Model of brain circuit stimulation with Izhikevich Model of cortical spiking neurons.

## Introduction

Physiological activity in the brain can be characterized mathematically. This is, essentially, the truncated foundation for computational neuroscience. Today, the field of computational neuroscience is vast, relying on well-layed work and novel findings to uncover the dynamics of the human brain.

## The action potential

Neurons produce action potentials, which are the basic "action" that each neuron produces. The scaffolding production of action potentials across the brain gives rise to cognitive processing. To stimulate an action potential, you can refer to the **Hodgkin-Huxley model**, which characterizes the total current flow throughout the cell membrane as...

$$
I = C_m \frac{dV_m}{d_t} + g_K(V_m - V_k) + g_{Na}(V_m -V_{Na}) + g_l(V_m =V_l)
$$

where $I$ is the entire current across the membrane, $C_m$ is the change in electric charge per unit area, $g_K$ and $g_{Na}$ are the potassium and sodium molecule conductants, $V_K$ and $V_{Na}$ are the potassium and sodium molecule reversal potentials, $g_l$ and $V_l$ are the leak conductance per unit area and leak reversal potential, respectively.

This model was first introduced in 1952 using a giant squid axon.

### A deeper look into the action potential

Action potentials are constant, in that their power remains the same. The baseline, or "resting state" is around -70 millivolts. After stimulation, or simple biological mechanisms (transferring of molecules across the membrane) the neuron undergoes a state of "depolarization" or increase in voltage, with a peak voltage of about 30 millivolts. Once it reaches this peak, the neuron begins to return to its original state throguh a process called "repolarization" where it dips below the resting state during the "refactory period". Once it has undergone this period, the neuron returns to its resting state, only to complete this over again.

This process remains constant. However, what is not constant is the frquenecy at which this process occurs. This is where the Izhikevich model comes into play, as it can account for the dynamic and varying firing patterns exhibited by biological mechanisms.

## The Izhikevich Model

Developed by Eugene Izhikevich in 2003, this model reflects the hetergenous nature of neurphysiological processes--and it does it in a simple manner. It makes use of a couple of equations...

$$
\frac{dv}{dt} = c_1v^2 + c_2v + c_3 - c_4u + c_5 I
$$

and

$$
\frac{du}{dt} = a(bv - u)
$$

and a non-linearity

$$
v \geq 30
$$

$$
v \rightarrow c
$$

$$
u \rightarrow u + d
$$

Let's dive into this more.

### Breaking down the equations.

$v$ is the membran potential in millivolts. $t$ is time in milliseconds. $\frac{du}{dt}$ is the time rate of change in membrane potential. $u$ is the recovery variable, which is the product of $v$ and $b$. $I$ is the external current from the input cell. The "non-linearity" essential resets the neuron after eat has reached it's peak amplitude. The values $a, b, c$ and $d$ determine the spike and burst patterns. The constants are $c_1 = 0.04 \frac{mV}{ms}, c_2 = 0.05 \frac{1}{ms}, c_3 = 140 \frac{mV}{ms}, c_4 = 1 \frac{1}{ms}, c_5 = 1 \frac{mV \cdot \Omega}{ms \cdot A \cdot ms}$.

## Where to now?

Let's check this out using Python and MATLAB! The Python code will be in the form of a Jupyter Notebook (.ipynb) and the MATLAB code will be in the standard MATLAB file (.m).

> [Simulating a brain circuit in Python!]()

> [Simulating a brain circuit in MATLAB!]()
