---
publish: 1
---

Think of the power series as a way to approximate a function near a specific point 𝑐c. For example, if you have a function 𝑓(𝑥)f(x) and you want to approximate it near 𝑥=𝑐x=c, you can write it as a power series:

𝑓(𝑥)=∑𝑛=0∞𝑎𝑛(𝑥−𝑐)𝑛f(x)=∑n=0∞​an​(x−c)n

Here, each term in the series adds a correction to the approximation. Near 𝑥=𝑐x=c, the terms (𝑥−𝑐)𝑛(x−c)n are small (since 𝑥x is close to 𝑐c), and the series converges to the function 𝑓(𝑥)f(x).

### Radius of Convergence

The series will only converge for values of 𝑥x within a certain distance from 𝑐c, called the radius of convergence 𝑅R. Within this radius, the series provides a good approximation of the function. Beyond this radius, the series may diverge.

### Example

For example, the Taylor series for 𝑒𝑥ex centered at 𝑥=0x=0 is:

𝑒𝑥=∑𝑛=0∞𝑥𝑛𝑛!ex=∑n=0∞​n!xn​

This series is centered at 𝑐=0c=0, meaning it expands from 𝑥=0x=0. For 𝑥x close to 0, the series converges to 𝑒𝑥ex. If we center the series at 𝑥=1x=1, it would look like:

𝑒𝑥=∑𝑛=0∞(𝑥−1)𝑛𝑛!𝑒ex=∑n=0∞​n!(x−1)n​e

In summary, the series expands from 𝑐c in the sense that it measures 𝑥x relative to 𝑐c and constructs the function's approximation around this point.

![[Idea of Expansion in Power Series-20240528140735744.webp]]