menu = '''
	[d] Depositar
	[s] Sacar
	[e] Extrato
	[q] Sair
'''

balance = 0
limit = 500
extract = ''
amount_of_withdrawals = 0
WITHDRAWAL_LIMIT = 3

template_operation = 'Valor do {}: de {} \n'
template_extract = '''
Olá este é seu extrato

Saldo em conta: R$ {}

Movimentações da conta:
{}
'''

while True:
	option = input(menu)
	message_warning = 'O valor para {} precisa ser positivo'
	message_instruction = 'Olá, qual o valor para {} ?  '
	message_success = '{} realizado(a) com sucesso, o que deseja fazer agora?'
	user_limit_diary = WITHDRAWAL_LIMIT

	if option.lower() == 'd':
		operation = 'deposito'.title()
		value = int(input(message_instruction.format(operation)))

		if value <= 0:
			print(message_warning.format(operation))
			continue
		else:
			balance += value
			extract += template_operation.format(operation, value)
			print(message_success.format(operation))

	if option.lower() == 's':
		operation = 'saque'.title()
		value = int(input(message_instruction.format(operation)))

		if value <= 0:
			print(message_warning.format(operation))
			continue
		elif value > balance:
			print(f'Saldo insuficiente para efetuar o {operation} deste valor')
			continue
		else:
			if user_limit_diary < 1:
				print(f'Simite de saque diário atingido')
				continue
			elif value > 500:
				print(f'O limite de valor por transação é de 500 por saque')
				continue
			else:
				balance -= value
				extract += template_operation.format(operation, value)
				user_limit_diary -= user_limit_diary
				print(message_success.format(operation))

	if option.lower() == 'e':
		operation = 'Consulta de extrato'.title()
		if balance == 0 and extract == '':
			print('Não foram realizadas movimentações')
		else:
			print(template_extract.format(balance, extract))
			print(message_success.format(operation))

	else:
	  print('Operação inválida, por favor selecione novamente operação desejada.')
