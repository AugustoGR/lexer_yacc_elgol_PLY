# Links relacionados

Artigo: https://docs.google.com/document/d/1AMLP_11kbz4_WVxqP3nd4V2oyD-q2jYHjsdMTIBzVtA/edit?usp=sharing

Apresentação: https://docs.google.com/presentation/d/1u5A9uAXuIcguYuip9pulekgl8Bu9_RGSBjOcbLXoqc0/edit?usp=sharing

# Setup para rodar

2. **Criar o ambiente**

   ```bash
   python -m venv venv
   ```

3. **Ativar ambiente virtual**
   **Windows:**

   ```bash
   venv\Scripts\activate
   ```

   **macOS/Linux:**

   ```bash
   source venv/bin/activate
   ```

4. **Instalar dependências**

   ```bash
   pip install -r requirements.txt
   ```

   **Sair do ambiente**

   ```bash
   deactivate
   ```

   **Rodar o código**

   ```bash
   cd src
   ```

   ```bash
   python3 .main.py
   ```

   ou

   ```bash
   python .main.py
   ```

   **Atenção**

   o grafo em png não vai funcionar sem a ferramenta graphviz
   caso esteja no linux instale a mesma via:

```bash
 sudo apt-get install graphviz
```

Caso esteja no windows instale o executável e configure a variável de ambiente.
