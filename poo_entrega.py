'''4 - Sistema de Cadastro de Pets em Clínica Veterinária
Registra pets, donos, histórico de consultas e vacinas. Útil para aplicar conceitos de herança e
composição'''

print('*** Pet System ***')

class Registro:
    def exibir_dados(self):
        raise NotImplementedError("Você precisa implementar 'exibir_dados()' na subclasse.")

class Dono(Registro):
    def __init__(self, nome, telefone):
        if len(nome) > 0:
            self.__nome = nome
        else:
            raise ValueError('Nome não pode ser vazio.')

        if len(telefone) > 0 and len(telefone) < 15:
            self.__telefone = telefone
        else:
            raise ValueError('Formato de telefone inválido. Use (xx)xxxxx-xxxx')

    def get_nome(self):
        return self.__nome

    def get_telefone(self):
        return self.__telefone

    def set_nome(self, novo_nome):
        if len(novo_nome) > 0:
            self.__nome = novo_nome
        else:
            raise ValueError('Nome não pode ser vazio.')

    def set_telefone(self, novo_telefone):
        if len(novo_telefone) > 0 and len(novo_telefone) < 15:
            self.__telefone = novo_telefone
        else:
            raise ValueError('Formato de telefone inválido. Use (xx)xxxxx-xxxx')

    def exibir_dados(self): 
        return f'Dono: {self.__nome} | Telefone: {self.__telefone}\n'

class Pet(Registro): 
    def __init__(self, nome_pet, raca, idade):
        if len(nome_pet) > 0:
            self._nome_pet = nome_pet
        else:
            raise ValueError('Nome não pode ser vazio.')

        if len(raca) > 0:
            self.__raca = raca
        else:
            raise ValueError('Digite a raça do pet.')

        if len(idade) >= 0:
            self.__idade = idade
        else:
            raise ValueError('Idade inválida. Digite um número válido.')

    def get_nome_pet(self):
        return self._nome_pet

    def get_raca(self):
        return self.__raca

    def get_idade(self):
        return self.__idade

    def set_nome_pet(self, novo_nome_pet):
        if len(novo_nome_pet) > 0:
            self._novo_nome_pet = novo_nome_pet
        else:
            raise ValueError('Nome não pode ser vazio.')

    def set_raca(self, nova_raca):
        if len(nova_raca) > 0:
            self.__nova_raca = nova_raca
        else:
            raise ValueError('Digite a raça do pet.')

    def set_idade(self, nova_idade):
        if len(nova_idade) > 0:
            self.__nova_idade = nova_idade
        else:
            raise ValueError('Idade inválida. Digite um número válido.')

    def exibir_dados(self):  
        return f'Pet: {self._nome_pet} | Raça: {self.__raca} | Idade: {self.__idade}\n'

class Vacinas(Registro): 
    def __init__(self, nome_vacina, data_vacina):
        self.nome_vacina = nome_vacina
        self.data_vacina = data_vacina

    def get_vacinas(self):
        return f'Vacina: {self.nome_vacina} | Data Vacinação: {self.data_vacina}\n'

    def exibir_dados(self):
        return self.get_vacinas()

class Consulta(Registro):
    def __init__(self, data, horario):
        self._data = data
        self._horario = horario

    def get_consulta(self):
        return f'Data da consulta: {self._data} | Horário: {self._horario}\n'

    def exibir_dados(self):
        return self.get_consulta()

class Sistema:
    def __init__(self):
        self.dono = []
        self.pet = []
        self.vacinas = []
        self.consulta = []

    def adicionar_dono(self, nome, telefone):
        try:
            novo = Dono(nome, telefone)
            self.dono.append(novo)
            print(f'Dono cadastrado com sucesso.\n')
        except ValueError as erro:
            print(f'Erro ao cadastrar dono: {erro}.')

    def adicionar_pet(self, nome_pet, raca, idade):
        try:
            novo_pet = Pet(nome_pet, raca, idade)
            self.pet.append(novo_pet)
            print(f'Pet cadastrado com sucesso.\n')
        except ValueError as erro:
            print(f'Erro ao cadastrar Pet: {erro}.')

    def adicionar_vacina(self, nome_vacina, data_vacina):
        try:
            vacina = Vacinas(nome_vacina, data_vacina)
            self.vacinas.append(vacina)
            print(f'Vacina cadastrada com sucesso.\n')
        except ValueError as erro:
            print(f'Erro ao cadastrar vacina: {erro}.')

    def adicionar_consulta(self, data, horario):
        try:
            consulta = Consulta(data, horario)
            self.consulta.append(consulta)
            print(f'Consulta agendada com sucesso.\n')
        except ValueError as erro:
            print(f'Erro ao cadastrar vacina: {erro}.')

    def exibir(self):
        for dono in self.dono:
            print(dono.exibir_dados())
        for pet in self.pet:
            print(pet.exibir_dados())

        print('*** Histórico de Vacinação ***\n')
        for vacina in self.vacinas:
            print(vacina.exibir_dados())

        print('*** Histórico de Consultas ***\n')
        for consulta in self.consulta:
            print(consulta.exibir_dados())

usuario1 = Sistema()
usuario1.adicionar_dono('Jota', '(19)98765-8765')
usuario1.adicionar_pet('Loló', 'Shitzu', '5')
usuario1.adicionar_vacina('Raiva', '12/05/2025')
usuario1.adicionar_consulta('13/05/2025', '13:30')
usuario1.adicionar_consulta('21/06/2024', '13:30')
usuario1.exibir()