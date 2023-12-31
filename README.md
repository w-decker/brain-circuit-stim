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

This process remains constant. However, what is not constant is the frquenecy at which this process occurs. Bursts of neuronal "spiking" is much less constant and requires further computations to model these dynamcics. This is where the Izhikevich model comes into play, as it can account for the dynamic and varying firing patterns exhibited by biological mechanisms.

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

$v$ is the membrane potential in millivolts. $t$ is time in milliseconds. $\frac{du}{dt}$ is the time rate of change in membrane potential. $u$ is the recovery variable, which is the product of $v$ and $b$. $I$ is the external current from the input cell. The "non-linearity" essential resets the neuron after eat has reached it's peak amplitude. The values $a, b, c$ and $d$ determine the spike and burst patterns. The constants are $c_1 = 0.04 \frac{mV}{ms}, c_2 = 0.05 \frac{1}{ms}, c_3 = 140 \frac{mV}{ms}, c_4 = 1 \frac{1}{ms}, c_5 = 1 \frac{mV \cdot \Omega}{ms \cdot A \cdot ms}$.

## Some more information about the nervous system.

In the nervous system exists a few different types of cells. Some are _excitatory_ and others are _inhibitory_. This means that some cells excite others while other inhibit others, but all cells emit an action potential. When modeling this, the parameters outlined above change slightly. Some remain constant across cell types and others differ. Let's see how these look if we were simulating a circuit of 1000 neurons.

| Excitatory cells                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Inhibitory cells                 | Description                                                              |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- | ------------------------------------------------------------------------ |
| $N_e$ = 800                       | 800 excitatory cells.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | $N_i$ = 200                      | 200 inhibitory cells                                                     |
| $a = 0.02$                        | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | $a = 0.02 + 0.08 \cdot U(0, 1)$  | parameters times uniformly distributed random number between 0 and 1.    |
| $b = 0.2$                         | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | $b = 0.25 - 0.5 \cdot U(0, 1)$   | ---                                                                      |
| $c = -65 + 15 \cdot U(0, 1)^2$    | voltage plus 15 times uniformly distributed random number between 0 and 1 squared.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | $c= -65$                         | ---                                                                      |
| $d = 8 - 6 \cdot U(0, 1)^2$       | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | $d = 2$                          | ---                                                                      |
| $v = -65$                         | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | $v = -65$                        | ---                                                                      |
| $u = b \cdot v$                   | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | $u = b \cdot v$                  | ---                                                                      |
| $S = 0.5 \cdot U(0, 1)[N, N_e]$   | We need our cells to be able to communicate with one another so this is a connectivity matrix. However, this matrix disobeys many biological factors and assumes that _all_ cells are connected to eachother. This matrix houses the weights of transmission between cells. You will concatenate the eexcitatory connectivity matrix with the inhibitory connectivity matrix to create a 1000X1000 matrix. In the excitatory component of the matrix, all numbers must be positive. If you notice, there is a scalar, $0.5$ which allows us to somewhat follow biological constructs, as excitatory cells are less powerful than inhibitory. | $S = -U(0, 1)[N, N_i]$           | In the inhibitory component of the matrix, all numbers must be negative. |
| $I = 5 \cdot N(0, 1) + S(fired) $ | The first terms prior to $S(fired)$ are exogenous input from the surrounding membrane environment. Then you must add all of the neurons that emitted an action potential (all those that _fired_) go to the rest of the neurons (because we have a 1:1 connectivity; all neurones are connected to all other neurons).                                                                                                                                                                                                                                                                                                                       | $I = 2 \cdot N(0, 1) + S(fired)$ | ---                                                                      |

## Where to now?

Let's check this out using Python and MATLAB! The Python code will be in the form of a Jupyter Notebook (.ipynb) and the MATLAB code will be in the standard MATLAB file (.m).

> [Simulating a brain circuit in Python!](/main.ipynb)

> [Simulating a brain circuit in MATLAB!](/main.m)

## Acknowledgements

This repo was created using resources from [Michael X. Cohen](https://www.udemy.com/course/python-scientific-x/), [Colombia University](http://www.columbia.edu/cu/appliedneuroshp/Spring2018/Spring18SHPAppliedNeuroLec5.pdf) and [Eugene Izhikevich](https://www.izhikevich.org/publications/spikes.htm).
