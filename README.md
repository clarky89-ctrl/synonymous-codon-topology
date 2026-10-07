# Synonymous Codon Graph Topology & Null Model Simulations

This repository contains the official Python implementation, network configuration models, and simulation data accompanying the manuscript:
**"Betti-1 of the Synonymous Codon Graph is Fixed by Degeneracy and Colinear with Conservative Edge Count"**

## 🔬 Overview
This project evaluates the topological features of the standard genetic code's synonymous codon graph. Recent network biology claims assert that the unweighted cycle rank (first Betti number, $\beta_1 = 27$) is an optimized trait under selective pressure. By deploying block-preserving null models, this framework demonstrates that $\beta_1$ is a rigid structural invariant of wobble degeneracy blocks rather than an adaptive anomaly. 

Additionally, this software models chemically weighted filtration graphs based on Polar Requirement (PR) differences to quantify the colinearity ($R^2 \approx 0.996$) between topological cycle counts $\beta_1(t)$ and raw conservative edge counts $E(t)$.

## 🛠️ Graph-Theoretic Foundations
The synonymous graph is mapped using the strict network rank formula:
$$\beta_1 = E_{syn} - V + C$$

Where the standard genetic code resolves strictly to:
$$\beta_1 = 67 - 61 + 21 = 27$$

### Causal Geometric Structural Breakdown:
* **5 × 4-Codon Boxes (Ala, Gly, Pro, Thr, Val):** Form complete four-vertex cliques ($K_4$), generating $V=4, E=6, C=1 \implies \beta_1 = 3$ cycles each (Total = 15).
* **2 × 6-Codon Connected Families (Leu, Arg):** Composed of a $K_4$ box and a $K_2$ pair connected by 2 parallel Hamming bridges, generating $V=6, E=9, C=1 \implies \beta_1 = 4$ cycles each (Total = 8).
* **1 × 6-Codon Split Family (Serine):** Due to a structural Hamming distance of 2, the TCN box and AGY pair are completely disconnected, creating $C=2$ components where $V=6, E=7 \implies \beta_1 = 3$ cycles.
* **1 × 3-Codon Family (Isoleucine):** Forms a complete triangle ($K_3$), generating $V=3, E=3, C=1 \implies \beta_1 = 1$ cycle.
* **9 × 2-Codon Families:** Line segments generating $\beta_1 = 0$.
* **2 × 1-Codon Families (Met, Trp):** Isolated vertices generating $\beta_1 = 0$.

## 📬 Contact
**James Clark** - Independent Scientist & Technology Engineer  
Email: clarky89@live.com
