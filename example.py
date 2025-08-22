#!/usr/bin/env python3
"""Example usage of Sublime embeddings."""

from embedings import Embeddings

def main():
    # Initialize with your project path
    print("Indexing codebase...")
    emb = Embeddings(".", supported_extensions={".py", ".md", ".txt"})
    
    print("\n" + "="*50)
    print("Semantic search example for file input/output operations")
    print("="*50)
    
    # Semantic search for complex concepts
    results = emb.search("file input output operations and data processing", top_n=1)
    for i, result in enumerate(results, 1):
        print(f"\nResult {i}: {result.file_path} (similarity: {result.max_similarity:.3f})")
        print("-" * 40)
        print(result)
    
    print("\n" + "="*50) 
    print("Neg/Pos search for functions that are not in classes.")
    print("="*50)
    
    # Find authentication code but exclude test code
    results = emb.search("def function(args)", 
                        negative_query="def function(self, argss)", top_n=1)
    for i, result in enumerate(results, 1):
        print(f"\nResult {i}: {result.file_path} (similarity: {result.max_similarity:.3f})")
        print("-" * 40)
        print(result)
    
    print("\n" + "="*50)
    print("Neg only search  against python code") 
    print("="*50)
    
    # Negative-only search for non-code
    results = emb.search(negative_query="code, python, logic", top_n=1)
    if results:
        print("Found potential technical debt:")
        for i, result in enumerate(results, 1):
            print(f"\nPotential issue {i}: {result.file_path} (dissimilarity: {result.max_similarity:.3f})")
            print("-" * 40)
            print(result)
    else:
        print("Great! No obvious technical debt found.")

if __name__ == "__main__":
    main()
