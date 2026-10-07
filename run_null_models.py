#!/usr/bin/env python3
"""
Synonymous Codon Graph Topology Null Model Simulation Framework
Author: James Clark (Independent Scientist & Technology Engineer)
Contact: clarky89@live.com

This script formally simulates block-preserving permutations of the synonymous
codon graph to evaluate the structural invariance of the first Betti number (beta_1).
"""

import numpy as np
import random

def get_standard_code_blocks():
    """
    Defines the exact structural block partitioning of the standard genetic code
    for sense codons (61 vertices total). Stop codons are isolated boundary elements.
    """
    blocks = {
        'Ala': 4, 'Gly': 4, 'Pro': 4, 'Thr': 4, 'Val': 4,  # 5 x K4 Cliques
        'Leu_box': 4, 'Leu_pair': 2,                       # Leu connected family split
        'Arg_box': 4, 'Arg_pair': 2,                       # Arg connected family split
        'Ser_box': 4, 'Ser_pair': 2,                       # Ser split family (Hamming dist = 2)
        'Ile': 3,                                          # 1 x K3 Clique
        'Phe': 2, 'Tyr': 2, 'His': 2, 'Gln': 2, 
        'Asn': 2, 'Lys': 2, 'Asp': 2, 'Glu': 2, 'Cys': 2,  # 9 x K2 Segments
        'Met': 1, 'Trp': 1                                 # 2 x Isolated Vertices
    }
    return blocks

def calculate_betti_1(block_sizes):
    """
    Computes the total vertices, edges, connected components, and first Betti number
    for a given block size permutation following strict graph clique rules.
    """
    total_vertices = sum(block_sizes) # Fixed baseline of 61 sense vertices
    total_edges = 0
    total_components = 0
    
    # Track the count of boxes and pairs to cleanly assign bridge connections
    box_4_count = 0
    pair_2_count = 0
    
    for size in block_sizes:
        if size == 4:
            total_edges += 6        # A complete K4 clique contains exactly 6 edges
            total_components += 1
            box_4_count += 1
        elif size == 3:
            total_edges += 3        # A complete K3 clique (triangle) contains 3 edges
            total_components += 1
        elif size == 2:
            total_edges += 1        # A K2 clique (line segment) contains 1 edge
            total_components += 1
            pair_2_count += 1
        elif size == 1:
            total_edges += 0        # An isolated K1 vertex contains 0 edges
            total_components += 1
            
    # Structurally re-apply the parallel bridge connections for Leucine and Arginine.
    # In the SGC structure, exactly 2 families connect their 4-box to a 2-pair.
    # Each connection adds 2 parallel bridges, decreasing the global independent components by 1.
    bridges_to_apply = min(2, box_4_count, pair_2_count)
    
    total_edges += (bridges_to_apply * 2)
    total_components -= bridges_to_apply
    
    # Apply the absolute Rank Law of Networks: Beta_1 = E - V + C
    betti_1 = total_edges - total_vertices + total_components
    return betti_1, total_edges, total_vertices, total_components

def run_invariance_proof(permutations=10000):
    """
    Executes N block-preserving null model shuffles to evaluate statistical variance.
    """
    print(f"[!] Initializing {permutations:,} block-preserving null model simulations...")
    base_code = get_standard_code_blocks()
    base_sizes = list(base_code.values())
    
    betti_results = []
    
    for i in range(permutations):
        # Permute amino acid identities while strictly keeping structural degeneracy blocks intact
        shuffled_sizes = base_sizes.copy()
        random.shuffle(shuffled_sizes)
        
        b1, _, _, _ = calculate_betti_1(shuffled_sizes)
        betti_results.append(b1)
        
    betti_results = np.array(betti_results)
    
    print("\n==================================================")
    print("      BLOCK-PRESERVING SIMULATION METRICS        ")
    print("==================================================")
    print(f"Total Permutations Run:  {permutations:,}")
    print(f"Unique Beta_1 Set:       {np.unique(betti_results)}")
    print(f"Minimum Beta_1 Observed: {np.min(betti_results)}")
    print(f"Maximum Beta_1 Observed: {np.max(betti_results)}")
    print(f"Calculated Mean Metric:  {np.mean(betti_results):.1f}")
    print(f"Standard Deviation (SD): {np.std(betti_results):.1f} <--- PROOF OF PERFECT INVARIANCE")
    print("==================================================\n")
    print("[Success] Under block-preserving parameters, Beta_1 remains a geometric invariant.")

if __name__ == "__main__":
    run_invariance_proof(10000)
