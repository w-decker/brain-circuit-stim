%% Simulating Brain circuit stimulation

% parameters
a = .02;
b = .2;
c = -50;
d = 2;

%constants
c1 = .04;
c2 = 5;
c3 = 140;

% initial membrane voltage
v = -65;

% recovery variable
u = b*v;

% create sample rate
time = 1000;
timevec = 1:1000;

% create empty membrane voltage vector
membrane_voltage = zeros(time);

% create scalar for each time point
I_all = zeros(time);

% loop over time
for i = 1:time
    % define input strength at timepoints
    if i > 200 && i < 400
        I = - 2;
    else 
        I = 7;
    end
    % check action potential
    if v >= 30
        v = c;
        u = u + d;
    end
    %update membrane variables
    v = v + c1*v^2 + c2*v + c3 - u + I;
    u = u + a*(b*v - u);
    % collects vars
    membrane_voltage(i) = v;
    I_all(i) = I;
end

% plot
figure(1), hold on
plot(membrane_voltage, 'color', 'k', 'LineWidth', 1)
legend(label='Membrane potential')
plot(I_all,'color', 'm' )
legend(label='Stimulation')
title("Simulation of 1 neuron")
xlabel('Time (ms)')
ylabel('Membran potential (mV)')
