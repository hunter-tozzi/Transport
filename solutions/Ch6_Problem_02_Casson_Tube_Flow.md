---
title: "Problem 2 — Casson Blood Flow in a Tube"
---

**Question**

The constitutive relationship for flow of blood in a cylinder of radius $R$ is

$$\left(\tau_{rz}\right)^{1/2} = \left(\tau_0\right)^{1/2} + \eta\left(\frac{dv_z}{dr}\right)^{1/2} \quad \text{for } \left|\tau_{rz}\right| > \tau_0 \qquad \frac{dv_z}{dr} = 0 \quad \text{for } \left|\tau_{rz}\right| \le \tau_0$$

(a) Show that the velocity profile is

$$r_c < r < R: \quad v_z = \frac{\Delta P R^2}{4\eta L}\left[\left(1 - \frac{r^2}{R^2}\right) - \frac{8}{3}\frac{r_c^{1/2}}{R^{1/2}}\left(1 - \frac{r^{3/2}}{R^{3/2}}\right) + \frac{2r_c}{R}\left(1 - \frac{r}{R}\right)\right]$$

$$0 < r < r_c: \quad v_z = \frac{\Delta P R^2}{4\eta L}\left[1 - \frac{8}{3}\frac{r_c^{1/2}}{R^{1/2}} + \frac{2r_c}{R} - \frac{r_c^2}{3R^2}\right]$$

where $r_c = 2\tau_0 L/\Delta P$ is the critical radius, at which the magnitude of the shear stress equals the yield stress.

(b) Show that the ratio of the wall shear stress, $\tau_w = \left|\tau_{rz}(r = R)\right|$, to the yield stress is

$$\frac{\tau_w}{\tau_0} = \frac{R}{r_c}$$

**Given:** the Casson-type constitutive relation, with yield stress $\tau_0$ and Casson viscosity $\eta$; tube radius $R$, length $L$ and pressure drop $\Delta P = P_0 - P_L$. No numerical values are given, so the solution stays symbolic.

**Additional assumptions:** steady, laminar, fully developed flow in a straight, rigid, horizontal tube; the flow is one-dimensional, $v_z = v_z(r)$; no slip at the wall, $v_z(R) = 0$.

**Form of the constitutive relation:** the relation is used here in the Casson form of Equations (4.31) and (4.33), with $\eta$ inside the square root

$$\tau_{rz}^{1/2} = \tau_0^{1/2} + \left(-\eta\frac{dv_z}{dr}\right)^{1/2} \quad \text{for } \left|\tau_{rz}\right| > \tau_0 \qquad \frac{dv_z}{dr} = 0 \quad \text{for } \left|\tau_{rz}\right| \le \tau_0$$

This corrects three points in the problem statement:

- The velocity decreases toward the wall, so $dv_z/dr < 0$. The square root must act on $-dv_z/dr$, as in Equation (4.31).
- The target profile has the prefactor $1/\eta$. That requires $\eta$ inside the square root, so that $S = \eta^{1/2}$ in Equation (4.31). With $\eta$ outside the root, as the problem writes it, the prefactor would be $1/\eta^2$.
- The second condition should read $\left|\tau_{rz}\right| \le \tau_0$, not $\left|\tau_{rz}\right| \le 0$.

## a Derive the velocity profile

### Shear-stress distribution

The shear-stress distribution in the tube follows from the momentum balance alone, for any fluid. Using Equation (6.43), with $\tau_{rz}$ finite on the centerline so that $C_3 = 0$, this gives Equation (6.44)

$$\tau_{rz} = \left(\frac{\Delta P}{2L}\right)r$$

The shear stress is zero on the centerline and increases linearly to the wall.

### Critical radius

The fluid yields only where $\left|\tau_{rz}\right| > \tau_0$. Set $\tau_{rz}(r_c) = \tau_0$

$$\left(\frac{\Delta P}{2L}\right)r_c = \tau_0 \qquad r_c = \frac{2\tau_0 L}{\Delta P}$$

For $r < r_c$, $\left|\tau_{rz}\right| < \tau_0$ and the fluid moves as an unsheared plug. For $r_c < r < R$, $\left|\tau_{rz}\right| > \tau_0$ and the fluid shears.

It is convenient to write the yield stress in terms of the critical radius

$$\tau_0 = \frac{\Delta P\,r_c}{2L}$$

### Velocity gradient in the sheared region

Substitute the shear-stress distribution into the constitutive relation for $r_c < r < R$

$$\left(\frac{\Delta P\,r}{2L}\right)^{1/2} = \tau_0^{1/2} + \left(-\eta\frac{dv_z}{dr}\right)^{1/2}$$

Isolate the velocity-gradient term and square both sides

$$-\eta\frac{dv_z}{dr} = \left[\left(\frac{\Delta P\,r}{2L}\right)^{1/2} - \tau_0^{1/2}\right]^2$$

Expand the square

$$-\frac{dv_z}{dr} = \frac{1}{\eta}\left[\frac{\Delta P\,r}{2L} - 2\left(\frac{\Delta P\,\tau_0}{2L}\right)^{1/2}r^{1/2} + \tau_0\right]$$

Replace $\tau_0$ with $\Delta P\,r_c/\left(2L\right)$. The middle coefficient becomes $\left(\Delta P\,\tau_0/2L\right)^{1/2} = \left(\Delta P^2 r_c/4L^2\right)^{1/2} = \Delta P\,r_c^{1/2}/\left(2L\right)$

$$-\frac{dv_z}{dr} = \frac{\Delta P}{2\eta L}\left[r - 2r_c^{1/2}r^{1/2} + r_c\right]$$

### Integrate with the no-slip condition

Integrate from a position $r$ in the sheared region to the wall, where $v_z(R) = 0$

$$v_z(R) - v_z(r) = \int_r^R\frac{dv_z}{dr'}\,dr' \qquad v_z(r) = \int_r^R\left(-\frac{dv_z}{dr'}\right)dr'$$

Substitute the gradient and integrate term by term

$$v_z(r) = \frac{\Delta P}{2\eta L}\left[\frac{r'^2}{2} - \frac{4}{3}r_c^{1/2}r'^{3/2} + r_c r'\right]_r^R$$

Evaluate between the limits

$$v_z(r) = \frac{\Delta P}{2\eta L}\left[\frac{R^2 - r^2}{2} - \frac{4}{3}r_c^{1/2}\left(R^{3/2} - r^{3/2}\right) + r_c\left(R - r\right)\right]$$

Factor out $R^2/2$, using $R^2 - r^2 = R^2\left(1 - r^2/R^2\right)$, $R^{3/2} - r^{3/2} = R^{3/2}\left(1 - r^{3/2}/R^{3/2}\right)$ and $R - r = R\left(1 - r/R\right)$

$$v_z(r) = \frac{\Delta P R^2}{4\eta L}\left[\left(1 - \frac{r^2}{R^2}\right) - \frac{8}{3}\frac{r_c^{1/2}}{R^{1/2}}\left(1 - \frac{r^{3/2}}{R^{3/2}}\right) + \frac{2r_c}{R}\left(1 - \frac{r}{R}\right)\right]$$

$$\boxed{r_c < r < R: \quad v_z = \frac{\Delta P R^2}{4\eta L}\left[\left(1 - \frac{r^2}{R^2}\right) - \frac{8}{3}\frac{r_c^{1/2}}{R^{1/2}}\left(1 - \frac{r^{3/2}}{R^{3/2}}\right) + \frac{2r_c}{R}\left(1 - \frac{r}{R}\right)\right]}$$

### Velocity in the plug region

For $0 < r < r_c$, $\left|\tau_{rz}\right| \le \tau_0$. Using Equation (4.33)

$$\frac{dv_z}{dr} = 0 \qquad v_z(r) = v_z(r_c)$$

The plug velocity equals the sheared-region velocity at $r = r_c$, because the velocity is continuous. Substitute $r = r_c$ into the sheared-region profile

$$v_z(r_c) = \frac{\Delta P R^2}{4\eta L}\left[1 - \frac{r_c^2}{R^2} - \frac{8}{3}\frac{r_c^{1/2}}{R^{1/2}} + \frac{8}{3}\frac{r_c^{1/2}r_c^{3/2}}{R^{1/2}R^{3/2}} + \frac{2r_c}{R} - \frac{2r_c^2}{R^2}\right]$$

Combine the $r_c^2/R^2$ terms: $-1 + \frac{8}{3} - 2 = -\frac{1}{3}$

$$\boxed{0 < r < r_c: \quad v_z = \frac{\Delta P R^2}{4\eta L}\left[1 - \frac{8}{3}\frac{r_c^{1/2}}{R^{1/2}} + \frac{2r_c}{R} - \frac{r_c^2}{3R^2}\right]}$$

**The core, $r < r_c$, moves as a solid plug** at uniform velocity, because the shear stress there is below the yield stress. The shear stress in the plug is not zero. It still increases linearly with $r$, as Equation (6.44) requires, but it is too small to make the fluid yield.

### Check the profile

- *No slip:* at $r = R$, every bracketed term is zero, so $v_z(R) = 0$.
- *Smooth join at $r_c$:* at $r = r_c$, $\left(\Delta P\,r_c/2L\right)^{1/2} - \tau_0^{1/2} = 0$, so $dv_z/dr = 0$ on both sides of $r_c$. The velocity and its slope are continuous.
- *Newtonian limit:* as $\tau_0 \to 0$, $r_c \to 0$ and the profile reduces to $v_z = \frac{\Delta P R^2}{4\eta L}\left(1 - \frac{r^2}{R^2}\right)$, the Poiseuille profile of Equation (6.49) with $\mu = \eta$.
- *No-flow limit:* as $r_c \to R$, the plug velocity bracket becomes $1 - \frac{8}{3} + 2 - \frac{1}{3} = 0$. Flow stops when the wall shear stress falls to the yield stress.
- *Units:* $\eta$ has units of $\mathrm{Pa\cdot s}$, so $\Delta P R^2/\left(\eta L\right)$ has units of $\mathrm{Pa\cdot m^2}/\left(\mathrm{Pa\cdot s\cdot m}\right) = \mathrm{m/s}$. The bracket is dimensionless.

## b Derive the wall-to-yield stress ratio

Evaluate the shear-stress distribution at the wall. Using Equation (6.45)

$$\tau_w = \left|\tau_{rz}(R)\right| = \frac{\Delta P\,R}{2L}$$

The yield stress, from the definition of the critical radius, is

$$\tau_0 = \frac{\Delta P\,r_c}{2L}$$

Divide the wall shear stress by the yield stress. The factor $\Delta P/\left(2L\right)$ cancels

$$\frac{\tau_w}{\tau_0} = \frac{\Delta P\,R/\left(2L\right)}{\Delta P\,r_c/\left(2L\right)}$$

$$\boxed{\frac{\tau_w}{\tau_0} = \frac{R}{r_c}}$$

**The ratio of wall shear stress to yield stress equals the ratio of tube radius to plug radius.** The plug fills a larger fraction of the tube as the wall shear stress approaches the yield stress, and flow stops ($r_c = R$) when $\tau_w = \tau_0$.

**Check against the source solution:** the final results match the target expressions, but the source has several errors:

- The constitutive relation needs $-dv_z/dr$ and $\eta$ inside the square root, as noted above. When the source squares its relation, $1/\eta$ should become $1/\eta^2$ for the form it wrote. The target profile is correct only for the form with $\eta$ inside the root.
- The source writes $v_z(R) - v_z(r) = +\frac{1}{\eta}\int[\cdots]^2dr$. Because $dv_z/dr < 0$, the correct statement is $v_z(r) - v_z(R) = \frac{1}{\eta}\int_r^R[\cdots]^2dr$.
- The middle term of the source's integral shows $\frac{4}{3}\frac{\Delta P\tau_0}{2L}r^{3/2}$. It should be $\frac{4}{3}\left(\frac{\Delta P\tau_0}{2L}\right)^{1/2}r^{3/2}$.
- The source says that in the plug "$\tau_{rz}$ is a constant". In fact $\tau_{rz}$ still varies linearly with $r$ there. It is the velocity that is constant, because $\left|\tau_{rz}\right| < \tau_0$.
- The source writes the wall shear stress as $\Delta P R/\left(rL\right)$. It should be $\Delta P R/\left(2L\right)$, as in Equation (6.45).
