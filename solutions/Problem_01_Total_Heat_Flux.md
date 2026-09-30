---
title: "Problem 1 – Total Heat Flux in a Flowing Fluid"
---

## Problem Statement

Warm saline (modeled as water) flows steadily through a small, heated channel of length $L = 0.10\ \mathrm{m}$. The flow is fully developed and one-dimensional in the $x$-direction. At the inlet ($x = 0$) the temperature is $T(0) = 300\ \mathrm{K}$, and at the outlet ($x = L$) the temperature is $T(L) = 310\ \mathrm{K}$.

Assume:

- The temperature varies linearly with $x$ between $0$ and $L$
- The velocity is uniform and constant: $v_x = 1.0\times10^{-3}\ \mathrm{m/s}$
- Fluid properties (saline): $\rho = 1000\ \mathrm{kg/m^3}$, $c_p = 4180\ \mathrm{J/(kg\cdot K)}$, $k = 0.60\ \mathrm{W/(m\cdot K)}$
- The reference temperature is $T_R = T(0) = 300\ \mathrm{K}$

Determine, using Equation (2.27):

1. Temperature profile and gradient
    - (a) The linear expression for $T(x)$ for $0 \le x \le L$
    - (b) The temperature gradient $dT/dx$
2. Heat flux at the midpoint $x = L/2$
    - (a) $T(L/2)$
    - (b) The convective contribution to the heat flux, $\rho v_x c_p (T - T_R)$, at $x = L/2$
    - (c) The conductive contribution to the heat flux, $-k\,dT/dx$
    - (d) The total heat flux $q_x^{\text{tot}}$ at $x = L/2$ and its direction
3. Relative importance: at $x = L/2$, the percentage of the total heat flux carried by convection and by conduction

## Solution

**Supplied information:** $L$, $T(0)$, $T(L)$, the linear temperature profile, the uniform velocity $v_x$, the properties $\rho$, $c_p$, $k$, and the reference temperature $T_R$.

**Additional assumptions:** steady state; the properties $\rho$, $c_p$ and $k$ are constant over the $300$–$310\ \mathrm{K}$ range; the positive $x$-direction is the flow direction (inlet to outlet). The channel walls supply the heat that raises the fluid temperature along the channel. This wall heating does not enter the flux calculation at a single location, so no wall heat rate is needed.

### Part 1 – Temperature Profile and Gradient

**Step 1. Write the general linear temperature profile (Part 1a).**
A linear profile passes through the two known end temperatures. Its slope is the temperature rise divided by the channel length:

$$T(x) = T(0) + \left(\frac{T(L) - T(0)}{L}\right)x$$

**Step 2. Substitute the given end temperatures and channel length.**
This step evaluates the slope with units:

$$T(x) = 300\ \mathrm{K} + \left(\frac{310\ \mathrm{K} - 300\ \mathrm{K}}{0.10\ \mathrm{m}}\right)x$$

$$T(x) = 300\ \mathrm{K} + \left(\frac{10\ \mathrm{K}}{0.10\ \mathrm{m}}\right)x$$

$$\boxed{T(x) = 300\ \mathrm{K} + \left(100\ \mathrm{K/m}\right)x \qquad 0 \le x \le 0.10\ \mathrm{m}}$$

Check: $T(0) = 300\ \mathrm{K}$ and $T(0.10\ \mathrm{m}) = 300\ \mathrm{K} + (100\ \mathrm{K/m})(0.10\ \mathrm{m}) = 310\ \mathrm{K}$. Both boundary values are recovered.

**Step 3. Differentiate the profile to obtain the temperature gradient (Part 1b).**
The constant term has zero derivative, so the gradient is the slope of the line:

$$\frac{dT}{dx} = \frac{d}{dx}\left[300\ \mathrm{K} + \left(100\ \mathrm{K/m}\right)x\right] = 0 + 100\ \mathrm{K/m}$$

$$\boxed{\frac{dT}{dx} = 100\ \mathrm{K/m}}$$

The gradient is positive and uniform: temperature increases in the $+x$ (flow) direction everywhere in the channel.

### Part 2 – Heat Flux at the Midpoint $x = L/2$

**Step 4. Locate the midpoint.**
This step gives the position at which all fluxes are evaluated:

$$x = \frac{L}{2} = \frac{0.10\ \mathrm{m}}{2} = 0.05\ \mathrm{m}$$

**Step 5. Evaluate the midpoint temperature (Part 2a).**
Substitute $x = 0.05\ \mathrm{m}$ into the profile from Step 2:

$$T\!\left(\frac{L}{2}\right) = 300\ \mathrm{K} + \left(100\ \mathrm{K/m}\right)\left(0.05\ \mathrm{m}\right) = 300\ \mathrm{K} + 5\ \mathrm{K}$$

$$\boxed{T\!\left(\frac{L}{2}\right) = 305\ \mathrm{K}}$$

**Step 6. Write the convective heat flux (Part 2b).**
The convective heat flux is the thermal energy, measured relative to $T_R$, carried by the bulk motion of the fluid. It is given by Equation (2.23):

$$q_x^{\text{conv}} = \rho v_x c_p \left(T - T_R\right)$$

**Step 7. Compute the temperature excess relative to the reference temperature.**

$$T - T_R = 305\ \mathrm{K} - 300\ \mathrm{K} = 5\ \mathrm{K}$$

**Step 8. Compute the mass flux $\rho v_x$.**
This is the convective mass flux of Equation (2.20), the mass crossing a unit area per unit time:

$$\rho v_x = \left(1000\ \mathrm{\frac{kg}{m^3}}\right)\left(1.0\times10^{-3}\ \mathrm{\frac{m}{s}}\right) = 1.0\ \mathrm{\frac{kg}{m^2\cdot s}}$$

**Step 9. Multiply by the specific heat.**
Use $1\ \mathrm{J/s} = 1\ \mathrm{W}$:

$$\rho v_x c_p = \left(1.0\ \mathrm{\frac{kg}{m^2\cdot s}}\right)\left(4180\ \mathrm{\frac{J}{kg\cdot K}}\right) = 4180\ \mathrm{\frac{J}{m^2\cdot s\cdot K}} = 4180\ \mathrm{\frac{W}{m^2\cdot K}}$$

**Step 10. Evaluate the convective heat flux.**

$$q_x^{\text{conv}} = \left(4180\ \mathrm{\frac{W}{m^2\cdot K}}\right)\left(5\ \mathrm{K}\right)$$

$$\boxed{q_x^{\text{conv}} = 20{,}900\ \mathrm{W/m^2} \quad \text{(in the } +x \text{ direction, with the flow)}}$$

The sign is positive because $v_x > 0$ and $T > T_R$: the warm fluid carries energy downstream.

**Step 11. Write and evaluate the conductive heat flux (Part 2c).**
The conductive (molecular) heat flux follows Fourier's law, Equation (2.9):

$$q_x = -k\frac{dT}{dx}$$

Substitute $k$ and the gradient from Step 3:

$$q_x = -\left(0.60\ \mathrm{\frac{W}{m\cdot K}}\right)\left(100\ \mathrm{\frac{K}{m}}\right) = -60\ \mathrm{\frac{W}{m^2}}$$

$$\boxed{q_x = -60\ \mathrm{W/m^2} \quad \text{(in the } -x \text{ direction, toward the colder inlet)}}$$

The negative sign means heat conducts down the temperature gradient, from the warmer outlet toward the cooler inlet, opposite to the flow.

**Step 12. Combine the two contributions to obtain the total heat flux (Part 2d).**
The total heat flux is the sum of the convective and conductive fluxes, Equation (2.27):

$$q_x^{\text{tot}} = \rho v_x c_p \left(T - T_R\right) + q_x = \rho v_x c_p \left(T - T_R\right) - k\frac{dT}{dx}$$

Substitute the results of Steps 10 and 11:

$$q_x^{\text{tot}}\!\left(\frac{L}{2}\right) = 20{,}900\ \mathrm{\frac{W}{m^2}} + \left(-60\ \mathrm{\frac{W}{m^2}}\right) = 20{,}840\ \mathrm{\frac{W}{m^2}}$$

$$\boxed{q_x^{\text{tot}}\!\left(\frac{L}{2}\right) = 20{,}840\ \mathrm{W/m^2} \approx 2.08\times10^{4}\ \mathrm{W/m^2} \quad \text{(in the } +x \text{ direction, downstream)}}$$

The positive total means that the net transport of thermal energy at the midpoint is downstream with the flow. Conduction opposes it only slightly.

### Part 3 – Relative Importance of Convection and Conduction

**Step 13. Form the sum of magnitudes used for comparison.**
The two contributions have opposite signs. Comparing each with the net total $20{,}840\ \mathrm{W/m^2}$ would give a convective share above $100\%$ and a negative conductive share. The shares are therefore based on the sum of the magnitudes of the two mechanisms:

$$\left|q_x^{\text{conv}}\right| + \left|q_x\right| = 20{,}900\ \mathrm{\frac{W}{m^2}} + 60\ \mathrm{\frac{W}{m^2}} = 20{,}960\ \mathrm{\frac{W}{m^2}}$$

**Step 14. Compute the convective fraction.**

$$\text{Fraction}_{\text{conv}} = \frac{\left|q_x^{\text{conv}}\right|}{\left|q_x^{\text{conv}}\right| + \left|q_x\right|} = \frac{20{,}900\ \mathrm{W/m^2}}{20{,}960\ \mathrm{W/m^2}} = 0.9971$$

**Step 15. Compute the conductive fraction.**

$$\text{Fraction}_{\text{cond}} = \frac{\left|q_x\right|}{\left|q_x^{\text{conv}}\right| + \left|q_x\right|} = \frac{60\ \mathrm{W/m^2}}{20{,}960\ \mathrm{W/m^2}} = 0.0029$$

Check: $0.9971 + 0.0029 = 1.0000$

$$\boxed{\text{Convection} \approx 99.7\% \qquad \text{Conduction} \approx 0.3\%}$$

For comparison, relative to the net total flux, convection is $20{,}900/20{,}840 = 100.3\%$ and conduction is $-60/20{,}840 = -0.3\%$. The conduction term reduces the net downstream flux by $0.3\%$. Either way, convection dominates.

**Step 16. Check units, signs and physical meaning.**

- *Units:* $\mathrm{(kg/m^3)(m/s)(J/(kg\cdot K))(K)} = \mathrm{J/(m^2\cdot s)} = \mathrm{W/m^2}$ for the convective term, and $\mathrm{(W/(m\cdot K))(K/m)} = \mathrm{W/m^2}$ for the conductive term. Both terms of Equation (2.27) have the units of heat flux.
- *Signs:* $v_x > 0$ and $T > T_R$ give positive convection. $dT/dx > 0$ gives negative conduction, pointing down the temperature gradient.
- *Physical meaning:* a Péclet-type ratio confirms the dominance of convection:

$$\frac{\rho v_x c_p \left(T - T_R\right)}{k\,\left(dT/dx\right)} = \frac{20{,}900\ \mathrm{W/m^2}}{60\ \mathrm{W/m^2}} \approx 348$$

Even at the slow speed of $1\ \mathrm{mm/s}$, convection carries about 350 times more thermal energy than conduction, because water's volumetric heat capacity $\rho c_p$ is large compared with its conductivity $k$.

- *Note on the reference temperature:* the convective term, and so the percentages in Part 3, depend on the chosen $T_R$. The conductive term does not. Choosing $T_R = T(0)$ measures energy relative to the inlet state, as the problem specifies.

- *Check against the source solution:* the given numerical results are correct. The source's Part 3 line "Convective fraction:" is left incomplete before the magnitude-based calculation; that calculation is completed in Steps 13–15.
