import secrets

import dummy as dummy

MESSAGE = b'gimme the flag'

if __name__ == '__main__':
	sk = secrets.token_bytes(16)
	pk = dummy.publickey_unsafe(sk)
	print(f'pk (hex): {pk.hex()}')
	while True:
		command = input('command: ')
		if command == 'sign':
			msg = bytes.fromhex(input('message (hex): '))
			if msg == MESSAGE:
				print('invalid message')
			else:
				sig = dummy.signature_unsafe(msg, sk, pk)
				print(dummy.checkvalid(sig, msg, pk))
				print(sig.hex())
		elif command == 'verify':
			sig = bytes.fromhex(input('signature (hex): '))
			try:
				dummy.checkvalid(sig, MESSAGE, pk)
				print(open('flag.txt').read().strip())
				break
			except:
				print('invalid signature')
		else:
			break
