import numpy as np;
import matplotlib.pyplot as pl;

t			= np.loadtxt('t.csv', delimiter=',');
quat_th		= np.loadtxt('quaternion_th.csv', delimiter=',');
omega_th 	= np.loadtxt('omega_th.csv', delimiter=',');

quat_pred 	= np.loadtxt('quaternion_pred.csv', delimiter=',');
omega_pred 	= np.loadtxt('omega_pred.csv', delimiter=',');
delta_t		= np.loadtxt('delta_t.csv', delimiter=',');

# plot quat_predict and omega_predict
pl.subplots(2,4, figsize=(10,7))
pl.suptitle("Quaternion")
pl.subplot(2,2,1)
pl.plot(t, quat_th[0,:], label='Theoretical')
pl.plot(t, quat_pred[0,:], label='Predicted')
pl.legend()
pl.xlabel("Time (s)")
pl.ylabel(r"$\eta$")
pl.grid(True)
pl.ylim(-1.1,1.1)
pl.legend()
pl.subplot(2,2,2)
pl.plot(t, quat_th[1,:], label='Theoretical')
pl.plot(t, quat_pred[1,:], label='Predicted')
pl.xlabel("Time (s)")
pl.ylabel(r"$\epsilon_x$")
pl.grid(True)
pl.ylim(-1.1,1.1)
pl.legend()
pl.subplot(2,2,3)
pl.plot(t, quat_th[2,:], label='Theoretical')
pl.plot(t, quat_pred[2,:], label='Predicted')
pl.xlabel("Time (s)")
pl.ylabel(r"$\epsilon_y$")
pl.grid(True)
pl.ylim(-1.1,1.1)
pl.legend()
pl.subplot(2,2,4)
pl.plot(t, quat_th[3,:], label='Theoretical')
pl.plot(t, quat_pred[3,:], label='Predicted')
pl.xlabel("Time (s)")
pl.ylabel(r"$\epsilon_z$")
pl.grid(True)
pl.ylim(-1.1,1.1)
pl.legend()

pl.subplots(2,4, figsize=(10,7))
pl.suptitle("Angular rate and timing")
pl.subplot(2,2,1)
pl.plot(t, omega_th[1,:], label='Theoretical')
pl.plot(t, omega_pred[1,:], label='Predicted')
pl.xlabel("Time (s)")
pl.ylabel(r"$\omega_x$")
pl.grid(True)
pl.legend()
pl.subplot(2,2,2)
pl.plot(t, omega_th[2,:], label='Theoretical')
pl.plot(t, omega_pred[2,:], label='Predicted')
pl.xlabel("Time (s)")
pl.ylabel(r"$\omega_y$")
pl.grid(True)
pl.legend()
pl.subplot(2,2,3)
pl.plot(t, omega_th[3,:], label='Theoretical')
pl.plot(t, omega_pred[3,:], label='Predicted')
pl.xlabel("Time (s)")
pl.ylabel(r"$\omega_z$")
pl.grid(True)
pl.legend()
pl.subplot(2,2,4)
pl.plot(t, delta_t, label='Raw')
avg = np.average(delta_t)
pl.plot(t, avg*np.ones(delta_t.size), label='Average = {:7.1f}'.format(avg))
pl.xlabel("Time (s)")
pl.ylabel(r"$\Delta_t$ (us)")
pl.grid(True)
pl.legend();

pl.show();
# print exec_time