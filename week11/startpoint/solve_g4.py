from Crypto.Util.number import bytes_to_long, long_to_bytes
import base64
import gmpy2

# Provided output: list of 9 base64-encoded (c, n) pairs
ciphertexts = [
    b'N4zfq1LqFq0XyBuk+ote4CEhcJc6V4rzZ2l+BffOkKSbs8z0rw6e2xjJZe6877UBC3voVrxVUyq+TcHgI6idPL39jdgWcIQMmqc7SB+dhKxlfoA2e81sXI88HunxGXm1DDrG1TYjJfqnd6PcyiumnOEHLqTMxU9ezG1RD4L8noE=tvCXY16L4hZJqVFX+ujC3ZMZThX9A3T9+tvVUIvqJeMUWaWQ74cXIakX1XwWiFvp0HchpnagMVg2a7+WWLeyZnBkAsz67f8dgr9ZTG0srqKRtr0RjdYdkt3TiSW9xV7lDTxe2qpjVCzk76SJyRtukqQ5vJK4lswqNt097zXdRmc=',
    b'FCXv7MoOHBSnBlQCl8osQiy9M36ltKx0+fS3m67sRCDnfvnkGzZlm5DuoHqjGYGlnYvyYvYENRsipUUbpj1Ltp8evr2DoWwlgz5uY1G8Ey6wMDKKUGKD3/R+RG9SCEBGxIGXjoU84Efr/NivDtL8FPp6TJaSPuk/+szMeFgbVfU=Q/DbbKtVKOpWbHIEkbD5hDI8q8SIqViaUCD4b6bZPicvJhh6HMTLah5c0VYqjfCb/DC25UysceaupHuz1PIB5C/aIBWOuPUk3Sxn7rQQyCEH/e7tJuKoXIX1CzmAfsdhwBAPJg6qXnEaBmA/djUVejXA5ozW1KUA2JwrSRIu4Uc=',
    b'YgsCVr2x898g7FTGrWfr2DBlsQna5ncqTxi2/+q1vEfaeh+i+E2k0l1PAx98yIu/cBTHHiUw72CKMkGtstrT0R+UTAJgQx4Zv3yggZsAmFKbhXoZKvYeyBJ7k5756tLvEhM6jwAaIwZZIq6H4UWrPPdnws01kNcetXVxfofJtvc=kvkp5i+7uQUreN/twzRQxi9svOsJzWR9HGlQZaOdBOvQqTanR6cY/4cvGAURQ+O8uRRXCDYVj00yXRPcj5h94Ypgyv2939Myu4JNPlK1gv6lsKiWBjRmpmuBdQlkUDEU+IevAOsEz+/2Hn+VoPy8LWfIgh/xDjyWmedDE7cQeg0=',
    b'LgdRuY9cFautSvJ69T5/lWcrXj+7rjdiouiE8PKqAH+Vs+On7UknRNY2vj6qvdG4RKj2nJ2fTLB3L1KpOIAcCrQfeTeySzK3MELCAt9/d83q606hH1Yu5BOaqIZd+LT5/5ZNrpavjtx2gkdE3huvoxbXXHtCs5MRUvD7rzjItKI=UT2Nl9RAw2UTcXInmNQDRRPllDN06cA9ze8njwIpD1oeoQR1XBi3NsASZrgEwvw9SPyFvi11J2YThpqTxO65LzLYeVCPBL3WfQXYRpCpnPQRUcl+NYnfqpz0E2+J8FJwcEUTKbKps1PWbHkbfaFhEfv7/fa71mai8+J5cDCXub0=',
    b'XkIZCpPAU00ci5lUuw3V9YXPmyzyzMwuzh+qGuuOXyjFrK+4vbDPbtQUkkYd381FACaUuBSs2e5RAYOph3A13uXUpuB4/RxxKa0O2J9e97OiFAgl/m3c7q74FKAUE4TxhGcYvt5HrsRkpDXu+jKkqJ3rw+gCgFTM7UrQYvyeH4E=f1PKG30Lx/D3bMNs7hVs+m+nbVc+/V6+qVpzxw1gfx9giNRTd/JTyHvfANcXCw/oh44S2ZVzJ7us1m4RzaZ8dq6U6YbWmA+MqEkLNGVGltNkXEmQBuqhSDgmYR/VOJv9de2hQ9JHaCwE7bkUyQlaqlrT3uZtxyzl2xeXrlfi3QU=',
    b'N2q0Sq/0OoA+xnI5RsYy09sKLxiq+u/qtxqSTcBddHzVZKFm5TJtLmp6HqnssOCC4TDtgSPv6WzOrt8WkqISBOw6CLMzVoWSgEKxGDME9Al1iTuRn3N7BHABnooYmFNnaKkLPhgqwxBNbpr8LsiU4OQWtRYF5XVd8UqFcClJ5Os=iAXRLhbAOXubR3q+Imi8aDXK0Ky67IZm1bRSMbjIaD2yGQspqNIJc4+yUEAJg7MU9hWdInmNFRaiYYpfwsSAhe2loyAlJSZdJlWB8RZMn+1FLxBWg2SvhkyhDfV4CqMmHIBcnccoeAPcBa3QIHQM5MFlOjG14CCxQOyxvtM0fgE=',
    b'mBzZjT2K19yWN3+H8hPyHPxTYUxRvzthmyiw2A1C146z3tg9pziJDLxD2Xs1R0wsjRaTNjOV0ehjIns68YJ+oFP4kOAsTjfbCFw0aqp4vA3gXayfAPnUe+ly/A6IfgN1fRBcc6PmC3FnnNUFLdVKZLmCGodborEUd5nb6pycHYQ=mv9htkOYAKUtzeBNxhsTmVEmT1nlNCQwatOHkh1L+/DMQ23XVY69BpPrc9zw8gm+NQbHqLmhpOPuO+4PaNAG2L0o+CXBrdwb9rK1Jr4XENQwEvxTLu3vnI+TmMsDSrkKkbORosgngE5wx6//RX0MAG3us7EzikGEFE2NO+rpJ60=',
    b'HwiuaEvmZo/oXbMotNmTkAngVxL1T51/5vyAzV4AxU7f3lLHsUWsx4ZGb2QFY+eDsXu4xDJ2OAtnQi4H70D7O/O8O0n1s2bkXeSnTnrLltOqfbnMCmRML360CrxeuqVMdVbHXjDsrhEk8swQ0PMARUk8S63Luc+uz8KwIUJFi98=cN4mo5zr3fAjND6cV/ZiJKwwtcQI9yRNO5Y1ekXSSLNdxrZql/O11hX33IgaCayDXhzJVd4Yxf88bM+wRzhyogPrzS91MuA0VeR1giPyBh+4s7vowyv0CluNoSoDmH10ONSyL/UMk6P+9CjoRsPetPZasw5jue6/yF/tZP7IX/0=',
    b'KyUt+T+H7ywRkKQbMHH5Y5CMQmnN8RRNbSvOF4FVeLAv2S4yg1DhCrYY0wiH4nGbZZvt63e3LCP2410I9wcWrgnQxyWS5cC/i3qUdJ2OeBDoF10t01+MVblJ6gMkTFToxZpDhrZ8YYRJfOwLeCtfnI5V+/LdlGbGo3NKZ3ajoqQ=q3yXqj/dZ+GFCcXXcacKh5zdFIK0duedPQNQMU2Jw5kpNkoufpKMI2nAyDfeWo+g/YpGltwyOuDP0SodgaGjGEQYyCczEKNdZIY682HG3SbR8BJ0MkAkfrK/djt7CQ8CzFbtoKy30ugO76Q07grzfMLdGnHnSLnT1qriBRowVEs='
]

def decode_base64_pair(encoded):
    """
    Decode a base64-encoded (c, n) pair by finding the boundary between c and n.
    """
    for i in range(len(encoded) // 2, len(encoded)):
        try:
            # Try decoding first part as base64 (ciphertext c)
            c_bytes = base64.b64decode(encoded[:i])
            # Try decoding second part as base64 (modulus n)
            n_bytes = base64.b64decode(encoded[i:])
            # Convert to integers
            c = bytes_to_long(c_bytes)
            n = bytes_to_long(n_bytes)
            return c, n
        except:
            continue
    raise ValueError("Could not find valid base64 boundary")

# Step 1: Decode all ciphertexts and moduli
c_n_pairs = [decode_base64_pair(cipher) for cipher in ciphertexts]
cs = [pair[0] for pair in c_n_pairs]  # List of ciphertexts c_i
ns = [pair[1] for pair in c_n_pairs]  # List of moduli n_i

# Step 2: Verify coprimality of moduli (optional, assuming they are coprime)
# For large random primes, coprimality is almost certain, but we could check GCD if needed.

# Step 3: Apply Chinese Remainder Theorem to solve c_i = m^7 mod n_i
def crt(a, n):
    """
    Chinese Remainder Theorem: Solve x = a_i mod n_i for x.
    a: list of remainders (c_i)
    n: list of moduli (n_i)
    Returns x such that x = a_i mod n_i for all i.
    """
    assert len(a) == len(n)
    N = 1
    for modulus in n:
        N *= modulus  # Compute product of all moduli
    result = 0
    for i in range(len(a)):
        Ni = N // n[i]  # N/n_i
        # Find modular inverse of Ni mod n_i
        Ni_inv = gmpy2.invert(Ni, n[i])
        result += a[i] * Ni * Ni_inv
    return result % N

# Compute C = m^7 mod (n_1 * n_2 * ... * n_9)
C = crt(cs, ns)

# Step 4: Compute m by taking the 7th root of C
# Since m^7 < n_1 * ... * n_9, C = m^7 exactly
m, exact = gmpy2.iroot(C, 7)
if not exact:
    raise ValueError("7th root is not exact, something went wrong")

# Step 5: Convert m back to bytes to get SECRET
SECRET = long_to_bytes(m)
print(f"Recovered SECRET: {SECRET}")

# Verify the result (optional)
for i, (c, n) in enumerate(c_n_pairs):
    assert pow(m, 7, n) == c, f"Verification failed for pair {i}"
print("Verification passed: m^7 mod n_i matches all c_i")