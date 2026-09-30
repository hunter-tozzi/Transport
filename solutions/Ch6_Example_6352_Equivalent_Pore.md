---
title: "Example 6.3.5.2 — Steady Flow Through an Equivalent Pore"
---

**Question**

Estimate the flow rate through an equivalent pore that spans a junction between endothelial cells in a capillary. The equivalent pore radius is $R_p = 20\ \mathrm{nm}$ and its length is $\Delta z = 100\ \mathrm{nm}$. The pressure on the plasma side of the pore is $20\ \mathrm{mmHg}$ higher than on the interstitial side. The principal plasma proteins contributing to the oncotic pressure are albumin (alb) and globulin (g). Their concentrations on the plasma (p) and interstitial (i) sides of the pore are:

- $C_{\text{alb},p} = 0.682\ \mathrm{mM}$ and $C_{g,p} = 0.192\ \mathrm{mM}$
- $C_{\text{alb},i} = 0.435\ \mathrm{mM}$ and $C_{g,i} = 0.083\ \mathrm{mM}$

The radii of albumin and globulin molecules are approximately $R_{\text{alb}} = 3.6\ \mathrm{nm}$ and $R_g = 4.5\ \mathrm{nm}$.

**Given:** $R_p$, $\Delta z$, the hydrostatic pressure difference $\Delta P = P_p - P_i = 20\ \mathrm{mmHg}$, the four protein concentrations and the two protein radii.

**Additional assumptions:**

- Flow through the pore is steady, laminar and fully developed, and the fluid is Newtonian.
- The viscosity is not given. As in the source, $\mu = 1\ \mathrm{cP} = 1.0\times10^{-3}\ \mathrm{Pa\cdot s}$ (water) is assumed. Plasma is closer to $1.2\ \mathrm{cP}$, which would lower the flow by about 17%.
- The proteins are rigid spheres.
- The temperature is $37\ ^\circ\mathrm{C}$.
- The osmotic virial coefficients are those used in the source, $A = 0.443\ \mathrm{mM^{-1}}$ and $B = 0.204\ \mathrm{mM^{-2}}$, which the source takes from an earlier example.

**Equations not on the slides:** the pore partition coefficient, the reflection coefficient of each solute and the combined reflection coefficient are textbook Equations (6.104), (6.107) and (6.108). They do not appear on the slides and are cited from the textbook as quoted in the example.

## 1 Write the Starling equation for the pore

Volumetric flow through a channel driven by hydrostatic and osmotic pressure differences follows the Starling relation. Using Equation (5.154), with side 1 the plasma and side 2 the interstitium

$$Q_V = K_f\left[\left(P_p - P_i\right) - \sigma_d\left(\Pi_p - \Pi_i\right)\right] = K_f\left(\Delta P - \sigma_d\,\Delta\Pi\right)$$

Here $K_f$ is the filtration coefficient, $\sigma_d$ the osmotic reflection coefficient and $\Delta\Pi$ the protein osmotic (oncotic) pressure difference. Each of the three must be estimated.

## 2 Calculate the filtration coefficient

For Poiseuille flow in a cylindrical pore, the filtration coefficient is the reciprocal of the flow resistance. Using Equation (6.53) with $R = R_p$ and $L = \Delta z$

$$K_f = \frac{1}{\Re} = \frac{\pi R_p^4}{8\mu\,\Delta z}$$

Convert the pore dimensions to meters

$$R_p = 20\ \mathrm{nm} = 2.0\times10^{-8}\ \mathrm{m} \qquad \Delta z = 100\ \mathrm{nm} = 1.0\times10^{-7}\ \mathrm{m}$$

Substitute

$$K_f = \frac{\pi\left(2.0\times10^{-8}\ \mathrm{m}\right)^4}{8\left(1.0\times10^{-3}\ \mathrm{Pa\cdot s}\right)\left(1.0\times10^{-7}\ \mathrm{m}\right)} = \frac{5.027\times10^{-31}\ \mathrm{m^4}}{8.0\times10^{-10}\ \mathrm{Pa\cdot s\cdot m}} = 6.283\times10^{-22}\ \mathrm{\frac{m^3}{Pa\cdot s}}$$

Convert to $\mathrm{mL/(mmHg\cdot s)}$, using $1\ \mathrm{m^3} = 10^6\ \mathrm{mL}$ and $1\ \mathrm{mmHg} = 133.322\ \mathrm{Pa}$

$$K_f = 6.283\times10^{-22}\ \mathrm{\frac{m^3}{Pa\cdot s}}\left(\frac{10^6\ \mathrm{mL}}{1\ \mathrm{m^3}}\right)\left(\frac{133.322\ \mathrm{Pa}}{1\ \mathrm{mmHg}}\right) = 8.38\times10^{-14}\ \mathrm{\frac{mL}{mmHg\cdot s}}$$

## 3 Calculate the partition and reflection coefficients

A spherical solute of radius $R_s$ can enter only the central part of the pore, where its center stays at least $R_s$ from the wall. The partition coefficient is the fraction of the pore cross-section available to the solute's center, textbook Equation (6.104)

$$\Phi_s = \left(1 - \frac{R_s}{R_p}\right)^2$$

For albumin and globulin

$$\Phi_{\text{alb}} = \left(1 - \frac{3.6\ \mathrm{nm}}{20\ \mathrm{nm}}\right)^2 = \left(0.820\right)^2 = 0.672 \qquad \Phi_g = \left(1 - \frac{4.5\ \mathrm{nm}}{20\ \mathrm{nm}}\right)^2 = \left(0.775\right)^2 = 0.601$$

The osmotic reflection coefficient of each solute is estimated from textbook Equation (6.107)

$$\sigma_{d,s} = \left(1 - \Phi_s\right)^2$$

$$\sigma_{d,\text{alb}} = \left(1 - 0.672\right)^2 = \left(0.328\right)^2 = 0.107 \qquad \sigma_{d,g} = \left(1 - 0.601\right)^2 = \left(0.399\right)^2 = 0.160$$

## 4 Calculate the protein osmotic pressures

The osmotic pressure of a nondilute protein solution follows the virial expansion of Equation (5.161). The part contributed by each protein $s$ is its share of that expansion, with the correction terms based on the total protein concentration $C_P$

$$\Pi_s = RT\,C_s\left(1 + A\,C_P + B\,C_P^2\right) \qquad C_P = C_{\text{alb}} + C_g$$

At $37\ ^\circ\mathrm{C}$, $RT = 19.3\ \mathrm{mmHg/mM}$, as in Equation (5.163). Calculate the total protein concentration on each side

$$C_{P,p} = 0.682\ \mathrm{mM} + 0.192\ \mathrm{mM} = 0.874\ \mathrm{mM} \qquad C_{P,i} = 0.435\ \mathrm{mM} + 0.083\ \mathrm{mM} = 0.518\ \mathrm{mM}$$

Evaluate the nonideality factor on each side

$$1 + 0.443\left(0.874\right) + 0.204\left(0.874\right)^2 = 1 + 0.3872 + 0.1558 = 1.5430 \quad \text{plasma}$$

$$1 + 0.443\left(0.518\right) + 0.204\left(0.518\right)^2 = 1 + 0.2295 + 0.0547 = 1.2842 \quad \text{interstitium}$$

Calculate the partial osmotic pressures

$$\Pi_{\text{alb},p} = \left(19.3\ \frac{\mathrm{mmHg}}{\mathrm{mM}}\right)\left(0.682\ \mathrm{mM}\right)\left(1.5430\right) = 20.31\ \mathrm{mmHg}$$

$$\Pi_{g,p} = \left(19.3\ \frac{\mathrm{mmHg}}{\mathrm{mM}}\right)\left(0.192\ \mathrm{mM}\right)\left(1.5430\right) = 5.72\ \mathrm{mmHg}$$

$$\Pi_{\text{alb},i} = \left(19.3\ \frac{\mathrm{mmHg}}{\mathrm{mM}}\right)\left(0.435\ \mathrm{mM}\right)\left(1.2842\right) = 10.78\ \mathrm{mmHg}$$

$$\Pi_{g,i} = \left(19.3\ \frac{\mathrm{mmHg}}{\mathrm{mM}}\right)\left(0.083\ \mathrm{mM}\right)\left(1.2842\right) = 2.06\ \mathrm{mmHg}$$

Form the osmotic pressure differences across the pore

$$\Delta\Pi_{\text{alb}} = 20.31\ \mathrm{mmHg} - 10.78\ \mathrm{mmHg} = 9.53\ \mathrm{mmHg}$$

$$\Delta\Pi_g = 5.72\ \mathrm{mmHg} - 2.06\ \mathrm{mmHg} = 3.66\ \mathrm{mmHg}$$

$$\Delta\Pi = \Delta\Pi_{\text{alb}} + \Delta\Pi_g = 9.53\ \mathrm{mmHg} + 3.66\ \mathrm{mmHg} = 13.19\ \mathrm{mmHg}$$

## 5 Calculate the combined reflection coefficient

The overall reflection coefficient weights each protein's coefficient by its share of the osmotic pressure difference, textbook Equation (6.108)

$$\sigma_d = \frac{\sigma_{d,\text{alb}}\,\Delta\Pi_{\text{alb}} + \sigma_{d,g}\,\Delta\Pi_g}{\Delta\Pi}$$

Substitute

$$\sigma_d = \frac{\left(0.107\right)\left(9.53\ \mathrm{mmHg}\right) + \left(0.160\right)\left(3.66\ \mathrm{mmHg}\right)}{13.19\ \mathrm{mmHg}} = \frac{1.023\ \mathrm{mmHg} + 0.584\ \mathrm{mmHg}}{13.19\ \mathrm{mmHg}} = 0.122$$

## 6 Calculate the flow through the pore

Calculate the effective driving pressure

$$\Delta P - \sigma_d\,\Delta\Pi = 20\ \mathrm{mmHg} - \left(0.122\right)\left(13.19\ \mathrm{mmHg}\right) = 20\ \mathrm{mmHg} - 1.61\ \mathrm{mmHg} = 18.39\ \mathrm{mmHg}$$

Substitute into the Starling equation, Equation (5.154)

$$Q_V = \left(8.38\times10^{-14}\ \mathrm{\frac{mL}{mmHg\cdot s}}\right)\left(18.39\ \mathrm{mmHg}\right)$$

Convert, using $1\ \mathrm{mL} = 10^{-6}\ \mathrm{m^3}$

$$\boxed{Q_V = 1.54\times10^{-12}\ \mathrm{mL/s} = 1.54\times10^{-18}\ \mathrm{m^3/s} \quad \text{from plasma to interstitium}}$$

**The flow is outward (filtration), from plasma to interstitial fluid**, because the hydrostatic pressure difference exceeds the effective oncotic opposition.

## 7 Interpret the reflection coefficient

Because $\sigma_d = 0.122$, only about 12% of the protein osmotic pressure difference opposes flow through this pore. The proteins are small compared with the $20\ \mathrm{nm}$ pore and pass through it relatively easily.

If the pore were smaller than an albumin molecule, both proteins would be fully reflected, $\sigma_d = 1$. The effective driving pressure would then fall to

$$\Delta P - \Delta\Pi = 20\ \mathrm{mmHg} - 13.19\ \mathrm{mmHg} = 6.81\ \mathrm{mmHg}$$

::: {custom-style="Answer Box"}
Only about 12% of the oncotic pressure difference acts across this 20 nm pore, so the net driving pressure is 18.4 mmHg. A pore that fully excluded the proteins (σd = 1) would cut the net driving pressure to 6.8 mmHg and the flow by a factor of about 2.7. Pores of different size exposed to the same ΔP and ΔΠ can therefore carry very different flows.
:::

**Check:** units of $K_f$: $\mathrm{m^4}/\left(\mathrm{Pa\cdot s\cdot m}\right) = \mathrm{m^3/(Pa\cdot s)}$, a flow per unit pressure, as required by Equation (5.154). $RT$ at $310\ \mathrm{K}$ is $\left(8.314\ \mathrm{J/(mol\cdot K)}\right)\left(310\ \mathrm{K}\right) = 2577\ \mathrm{Pa/mM} = 19.3\ \mathrm{mmHg/mM}$, consistent with Equation (5.163). The mean velocity in the pore, $Q_V/\left(\pi R_p^2\right) = 1.2\ \mathrm{mm/s}$, gives a Reynolds number far below 1, so laminar Poiseuille flow is appropriate.

**Check against the source solution:** the flow rate, $1.54\times10^{-12}\ \mathrm{mL/s}$, is correct. Three corrections:

- Rounding $\Delta\Pi_{\text{alb}}$ to $9.5\ \mathrm{mmHg}$ gives the source's $\Delta\Pi = 13.16\ \mathrm{mmHg}$. Without that rounding it is $13.19\ \mathrm{mmHg}$. The effect on the final flow is negligible.
- The source says the net driving force falls "from 18.7 mmHg to 6.84 mmHg" when $\sigma_d = 1$. The starting value is its own effective pressure, $20 - \left(0.122\right)\left(13.16\right) = 18.4\ \mathrm{mmHg}$, not $18.7\ \mathrm{mmHg}$.
- The viscosity of $1\ \mathrm{cP}$ is an assumption not stated in the problem.
