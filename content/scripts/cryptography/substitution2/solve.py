# Module used: https://pypi.org/project/cipher-solver/

from cipher_solver.simple import SimpleSolver

with open("message.txt", "r") as f:
    ciphertext = f.read()

solver = SimpleSolver(ciphertext)

solver.solve()

print("Decrypted text:")
print(solver.plaintext())

print("\nDecryption key:")
print(solver.decryption_key())
