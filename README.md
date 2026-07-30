# 🔒 Gerador de Senha

Interface web retrô (terminal CRT verde-fósforo) para o gerador de senha
original — mesma lógica de geração, agora com uma tela pra gerar e copiar.

## O que mudou em relação ao script original

- **Segurança**: `random.randint` trocado por `secrets.choice`. O módulo
  `random` do Python usa um gerador pseudoaleatório (Mersenne Twister) —
  bom para simulações e jogos, mas **previsível o suficiente para ser
  reconstruído por quem observa outras saídas dele**, o que o torna
  inadequado para gerar senhas. `secrets` é o módulo do Python feito
  especificamente para isso (tokens, senhas, chaves).
- O conjunto de caracteres é o mesmo do original (`chr(33)` a `chr(125)`) —
  só a fonte de aleatoriedade mudou, não o resultado possível.
- Virou uma interface web (Flask) com dois botões: gerar e copiar. De
  propósito, nada além disso — sem histórico, sem opções de
  maiúsculas/números/símbolos separadas, sem indicador de força. Se quiser
  qualquer uma dessas depois, é uma adição pequena.

## Como rodar

### Docker

```bash
docker compose up -d --build
```

### Python direto

```bash
pip install -r requirements.txt
python app.py
```

Acesse **http://localhost:5100**.

## Adicionando na Oficina

```python
{
    "id": "password-generator",
    "codigo": "PG-01",
    "nome": "Gerador de Senha",
    "tagline": "Gera senhas aleatórias com o módulo criptográfico do Python.",
    "descricao": "Interface retrô em terminal CRT para gerar e copiar senhas — usa secrets.choice, não random.randint.",
    "status": "estável",
    "tags": ["Python", "Flask", "Segurança"],
    "url_env": "PASSWORD_GENERATOR_URL",
    "url_default": "http://localhost:5100",
    "embeddable": True,
}
```
