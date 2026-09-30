---
title: "Problem 11 — Arteriolar Radius and Control of Arterial Blood Pressure"
---

**Question**

Blood flow to a resting skeletal muscle bed is supplied at mean arterial pressure $P_a = 95\ \mathrm{mmHg}$ and drains to venous pressure $P_v = 5\ \mathrm{mmHg}$. The dominant adjustable resistance in this vascular bed comes from small arterioles that can change radius by smooth muscle contraction (vasoconstriction) or relaxation (vasodilation). Assume:

- There are $N = 5000$ identical arterioles in parallel
- Each arteriole has length $L = 1.2\ \mathrm{mm}$
- Blood viscosity is $\mu = 3.5\times10^{-3}\ \mathrm{Pa\cdot s}$
- Baseline total flow to the bed is $Q_{\text{tot},0} = 12\ \mathrm{mL/min}$

1. Determine the baseline arteriole radius $R_0$ that produces the observed flow and pressure drop
2. The arterioles constrict by 15% in radius due to sympathetic activation
    - (a) What is the new resistance of one arteriole?
    - (b) What is the new total blood flow to the bed if arterial and venous pressures remain unchanged?
3. If instead the arterioles dilate by 20% from baseline, what is the new total flow?
4. Explain why arterioles are called "resistance vessels" in the control of arterial pressure

**Given:** $P_a$, $P_v$, $N$, $L$, $\mu$ and $Q_{\text{tot},0}$ as listed; the arterioles are identical and in parallel; $P_a$ and $P_v$ stay fixed when the radius changes.

**Additional assumptions:** the whole pressure drop $P_a - P_v$ acts across the arterioles, which are the dominant resistance; each arteriole carries steady, laminar, fully developed Poiseuille flow of a Newtonian fluid with the given viscosity, so Equation (6.53) applies; the viscosity and length do not change when the radius changes.

## Convert the given values

Pressure drop across the bed, using $1\ \mathrm{mmHg} = 133.322\ \mathrm{Pa}$

$$\Delta P = P_a - P_v = 95\ \mathrm{mmHg} - 5\ \mathrm{mmHg} = 90\ \mathrm{mmHg}$$

$$\Delta P = 90\ \mathrm{mmHg}\left(\frac{133.322\ \mathrm{Pa}}{1\ \mathrm{mmHg}}\right) = 1.200\times10^{4}\ \mathrm{Pa}$$

Baseline total flow, using $1\ \mathrm{mL} = 10^{-6}\ \mathrm{m^3}$ and $1\ \mathrm{min} = 60\ \mathrm{s}$

$$Q_{\text{tot},0} = 12\ \frac{\mathrm{mL}}{\mathrm{min}}\left(\frac{10^{-6}\ \mathrm{m^3}}{1\ \mathrm{mL}}\right)\left(\frac{1\ \mathrm{min}}{60\ \mathrm{s}}\right) = 2.0\times10^{-7}\ \mathrm{m^3/s}$$

Arteriole length

$$L = 1.2\ \mathrm{mm}\left(\frac{1\ \mathrm{m}}{1000\ \mathrm{mm}}\right) = 1.2\times10^{-3}\ \mathrm{m}$$

## 1 Determine the baseline arteriole radius

The resistance of the whole bed is the pressure drop divided by the flow. Using the first equality of Equation (6.53)

$$\Re_{\text{eq},0} = \frac{\Delta P}{Q_{\text{tot},0}} = \frac{1.200\times10^{4}\ \mathrm{Pa}}{2.0\times10^{-7}\ \mathrm{m^3/s}} = 6.0\times10^{10}\ \mathrm{Pa\cdot s/m^3}$$

For $N$ identical resistances in parallel, the reciprocals add, as for electrical resistors in parallel. This relation does not appear on the slides as a numbered equation

$$\frac{1}{\Re_{\text{eq}}} = \sum_{i=1}^{N}\frac{1}{\Re_i} = \frac{N}{\Re} \qquad \Re = N\,\Re_{\text{eq}}$$

Resistance of one arteriole

$$\Re_0 = N\,\Re_{\text{eq},0} = \left(5000\right)\left(6.0\times10^{10}\ \mathrm{Pa\cdot s/m^3}\right) = 3.0\times10^{14}\ \mathrm{Pa\cdot s/m^3}$$

Relate the single-arteriole resistance to its radius. Using the second equality of Equation (6.53)

$$\Re_0 = \frac{8\mu L}{\pi R_0^4}$$

Solve for the radius

$$R_0 = \left(\frac{8\mu L}{\pi\Re_0}\right)^{1/4}$$

Substitute the viscosity, length and resistance

$$R_0 = \left(\frac{8\left(3.5\times10^{-3}\ \mathrm{Pa\cdot s}\right)\left(1.2\times10^{-3}\ \mathrm{m}\right)}{\pi\left(3.0\times10^{14}\ \mathrm{Pa\cdot s/m^3}\right)}\right)^{1/4} = \left(\frac{3.36\times10^{-5}\ \mathrm{Pa\cdot s\cdot m}}{9.42\times10^{14}\ \mathrm{Pa\cdot s/m^3}}\right)^{1/4}$$

$$R_0 = \left(3.57\times10^{-20}\ \mathrm{m^4}\right)^{1/4}$$

$$\boxed{R_0 = 1.37\times10^{-5}\ \mathrm{m} = 13.7\ \mu\mathrm{m}}$$

**The baseline arteriole radius is about 14 μm** (diameter about 27 μm), which is typical of small arterioles.

## 2 Vasoconstriction by 15% in radius

### a Calculate the new resistance of one arteriole

The constricted radius is 85% of the baseline radius

$$R_1 = 0.85\,R_0$$

From Equation (6.53), at fixed $\mu$ and $L$ the resistance varies as $1/R^4$. Form the ratio of the constricted to the baseline resistance

$$\frac{\Re_1}{\Re_0} = \left(\frac{R_0}{R_1}\right)^4 = \left(\frac{1}{0.85}\right)^4 = \frac{1}{0.5220} = 1.916$$

Multiply by the baseline single-arteriole resistance

$$\Re_1 = 1.916\left(3.0\times10^{14}\ \mathrm{Pa\cdot s/m^3}\right)$$

$$\boxed{\Re_1 = 5.75\times10^{14}\ \mathrm{Pa\cdot s/m^3}}$$

**A 15% reduction in radius nearly doubles the resistance of each arteriole.**

### b Calculate the new total flow

The equivalent resistance of the bed rises by the same factor

$$\Re_{\text{eq},1} = \frac{\Re_1}{N} = \frac{5.75\times10^{14}\ \mathrm{Pa\cdot s/m^3}}{5000} = 1.15\times10^{11}\ \mathrm{Pa\cdot s/m^3}$$

With $\Delta P$ unchanged, the flow follows from Equation (6.53)

$$Q_{\text{tot},1} = \frac{\Delta P}{\Re_{\text{eq},1}} = \frac{1.200\times10^{4}\ \mathrm{Pa}}{1.15\times10^{11}\ \mathrm{Pa\cdot s/m^3}} = 1.044\times10^{-7}\ \mathrm{m^3/s}$$

Convert to $\mathrm{mL/min}$

$$Q_{\text{tot},1} = 1.044\times10^{-7}\ \frac{\mathrm{m^3}}{\mathrm{s}}\left(\frac{10^{6}\ \mathrm{mL}}{1\ \mathrm{m^3}}\right)\left(\frac{60\ \mathrm{s}}{1\ \mathrm{min}}\right)$$

$$\boxed{Q_{\text{tot},1} = 1.04\times10^{-7}\ \mathrm{m^3/s} = 6.3\ \mathrm{mL/min}}$$

Check with the fourth-power scaling directly: $Q_{\text{tot},1} = \left(0.85\right)^4 Q_{\text{tot},0} = \left(0.5220\right)\left(12\ \mathrm{mL/min}\right) = 6.26\ \mathrm{mL/min}$

**Blood flow to the bed falls by about 48%**, nearly half, for only a 15% reduction in radius.

## 3 Vasodilation by 20% in radius

The dilated radius is 120% of the baseline radius

$$R_2 = 1.20\,R_0$$

Form the resistance ratio

$$\frac{\Re_2}{\Re_0} = \left(\frac{R_0}{R_2}\right)^4 = \left(\frac{1}{1.20}\right)^4 = \frac{1}{2.0736} = 0.4823$$

The equivalent resistance of the bed decreases by the same factor

$$\Re_{\text{eq},2} = 0.4823\left(6.0\times10^{10}\ \mathrm{Pa\cdot s/m^3}\right) = 2.89\times10^{10}\ \mathrm{Pa\cdot s/m^3}$$

Calculate the new flow with $\Delta P$ unchanged

$$Q_{\text{tot},2} = \frac{\Delta P}{\Re_{\text{eq},2}} = \frac{1.200\times10^{4}\ \mathrm{Pa}}{2.89\times10^{10}\ \mathrm{Pa\cdot s/m^3}} = 4.15\times10^{-7}\ \mathrm{m^3/s}$$

Convert to $\mathrm{mL/min}$

$$Q_{\text{tot},2} = 4.15\times10^{-7}\ \frac{\mathrm{m^3}}{\mathrm{s}}\left(\frac{10^{6}\ \mathrm{mL}}{1\ \mathrm{m^3}}\right)\left(\frac{60\ \mathrm{s}}{1\ \mathrm{min}}\right)$$

$$\boxed{Q_{\text{tot},2} = 4.15\times10^{-7}\ \mathrm{m^3/s} = 24.9\ \mathrm{mL/min}}$$

Check with the fourth-power scaling directly: $Q_{\text{tot},2} = \left(1.20\right)^4 Q_{\text{tot},0} = \left(2.0736\right)\left(12\ \mathrm{mL/min}\right) = 24.9\ \mathrm{mL/min}$

**Blood flow to the bed more than doubles** (a 107% increase) for a 20% increase in radius.

## 4 Explain why arterioles are "resistance vessels"

::: {custom-style="Answer Box"}
Poiseuille resistance varies as 1/R⁴, Equation (6.53), so small changes in arteriole radius produce large changes in resistance: a 15% constriction nearly doubles it, and a 20% dilation halves it. Arterioles also carry most of the resistance of the circulation and have smooth-muscle walls that can change their radius actively. Mean arterial pressure equals cardiac output times total peripheral resistance, so arteriolar constriction raises total resistance and arterial pressure, while dilation lowers them. Arterioles are therefore the main site where the body adjusts both arterial pressure and the distribution of blood flow to individual tissues.
:::

**Check:** units of $\Re$ in Equation (6.53): $\mathrm{(Pa\cdot s)(m)}/\mathrm{m^4} = \mathrm{Pa\cdot s/m^3}$, consistent with $\Delta P/Q$. Each arteriole carries $Q_{\text{tot},0}/N = 4.0\times10^{-11}\ \mathrm{m^3/s}$ at a mean velocity of about $6.7\ \mathrm{cm/s}$. For a blood density near $1050\ \mathrm{kg/m^3}$ (assumed), the Reynolds number based on the diameter is about $0.6$, so laminar Poiseuille flow is a sound assumption.

**Check against the source solution:** the source's baseline radius, $13.7\ \mu\mathrm{m}$, is correct. Three corrections:

- For part 2(a), the source reports only the equivalent resistance of the bed, $1.15\times10^{11}\ \mathrm{Pa\cdot s/m^3}$. The question asks for the resistance of one arteriole, which is $5.75\times10^{14}\ \mathrm{Pa\cdot s/m^3}$.
- The constricted flow rounds to $6.3\ \mathrm{mL/min}$, not $6.2\ \mathrm{mL/min}$.
- For part 3, the source rounds the resistance ratio to $0.48$ and the equivalent resistance to $2.9\times10^{10}\ \mathrm{Pa\cdot s/m^3}$. That rounding gives $24.6\ \mathrm{mL/min}$ instead of the correct $\left(1.20\right)^4\left(12\ \mathrm{mL/min}\right) = 24.9\ \mathrm{mL/min}$.

**Model note:** assigning the entire $90\ \mathrm{mmHg}$ drop to arterioles only $1.2\ \mathrm{mm}$ long implies a wall shear stress of $\Delta P R_0/\left(2L\right) \approx 69\ \mathrm{Pa}$ ($690\ \mathrm{dyn/cm^2}$), from Equation (6.45). That is far above physiological values. In a real vascular bed, the pressure drop is shared among arteries, arterioles, capillaries and venules. The model still captures the key point: flow changes with the fourth power of arteriolar radius.
