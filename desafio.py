menu = '''
	[d] Depositar
	[s] Sacar
	[e] Extrato
	[q] Sair
'''

WITHDRAWAL_LIMIT = 3
balance = 0.0
limit = 500
amount_of_withdrawals = 0
user_limit_diary = WITHDRAWAL_LIMIT

account_movements = False

template_operation = 'Valor do {}: de R$ {} \n'
message_warning = 'O valor para {} precisa ser positivo'
message_instruction = 'Olá, qual o valor para {} ?  '
message_success = '{} realizado(a) com sucesso, o que deseja fazer agora?'
template_extract = '''
=====Olá este é seu extrato =====

Saldo em conta: R$ {}

Movimentações da conta:
'''

while True:
	option = input(menu)

	if option.lower() == 'd':
		operation = 'deposito'.title()
		value = float(input(message_instruction.format(operation)))

		if value <= 0:
			print(message_warning.format(operation))
			continue
		else:
			balance += value
			value = f'{value:.2f}'
			template_extract += template_operation.format(operation, value)
			account_movements = True
			print(message_success.format(operation))

	elif option.lower() == 's':
		operation = 'saque'.title()
		value = float(input(message_instruction.format(operation)))

		if (value <= 0) or (balance == 0):
			print(f'Saldo insuficiente para efetuar o {operation} deste valor')
			continue
		elif value > balance:
			print(f'Saldo insuficiente para efetuar o {operation} deste valor')
			continue
		else:
			if (user_limit_diary < 1) or (value > 500):
				print(f'Limite atingido, limite diário: ({WITHDRAWAL_LIMIT}) saques, limite por saque: (500)')
				continue
			else:
				balance -= value
				value = f'{value:.2f}'
				template_extract += template_operation.format(operation, value)
				user_limit_diary -= 1
				account_movements = True
				print(message_success.format(operation))

	elif option.lower() == 'e':
		operation = 'Consulta de extrato'.title()
		if account_movements == False:
			print('Não foram realizadas movimentações')
		else:
			balance_extract = f'{balance:.2f}'
			print(template_extract.format(balance_extract))
			print(message_success.format(operation))

	elif option.lower() == 'q':
		break
	else:
	  	print('Operação inválida, por favor selecione novamente operação desejada.')
