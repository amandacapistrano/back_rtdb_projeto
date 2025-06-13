# 🎵 Projeto de Recomendação Musical

Aplicação fullstack integrando **React Native** (front-end) com **Python FastAPI** (back-end) e **Firebase Realtime Database** para recomendar músicas com base no gênero musical preferido do usuário.

---

## 🧠 Tecnologias Utilizadas

- **Front-end:** React Native (com Expo)
- **Back-end:** Python com FastAPI
- **Banco de dados:** Firebase Realtime Database
- **API externa:** Deezer API (para buscar músicas)

---

## 📂 Repositórios e Links

- 🔧 **Repositório do back-end:**  
  [github.com/amandacapistrano/back_rtdb_projeto](https://github.com/amandacapistrano/back_rtdb_projeto)

- 🔗 **Documentação da API (Swagger):**  
  [https://back-rtdb-projeto.onrender.com/docs](https://back-rtdb-projeto.onrender.com/docs)

- 🔥 **Firebase Realtime Database:**  
  [Ver dados no Firebase](https://console.firebase.google.com/u/1/project/aula-b7426/database/aula-b7426-default-rtdb/data?hl=pt-br)

### 🚀 Como rodar o projeto:
- 📱 **Link do front-end no Snack (Expo):**  
  [Abrir no Expo Snack](https://snack.expo.dev/@amandacaps/projeto-com-fastapi-13-6)

---

## 🧾 Estrutura do Firebase

```json
{
  "users": {
    "<id_aleatorio>": {
      "criado_em": "2025-06-13T15:07:05.459528",
      "nome": "Amanda",
      "email": "amanda@test.com",
      "genero": "Pop",
      "musica_recomendada": {
        "titulo": "Musica",
        "artista": "Artista",
        "link": "https://www.deezer.com/track/...",
        "preview": "https://..."
      }
    }
  }
}
```
---
## ✅ Funcionalidades
- Cadastro de usuários com nome, email e gênero musical preferido e a recomendação

- Recomendação de uma música com base no gênero escolhido (via API Deezer)

- Armazenamento da recomendação no Firebase

- Listagem dos últimos usuários cadastrados com botão para deletar o dado

- Visualização e abertura do link da música recomendada
---
### 📌 Observação
- Os links de músicas retornados pela API Deezer podem depender de disponibilidade.
- API no Render pode passar por perído de inatividade.
