## Aplicação React + Python
- Repositório do back-end (endpoints hospendados no render): https://github.com/amandacapistrano/back_rtdb_projeto

- Link endpoints: 
https://back-rtdb-projeto.onrender.com/docs

- RealTime database:
https://console.firebase.google.com/u/1/project/aula-b7426/database/aula-b7426-default-rtdb/data?hl=pt-br

*Estrutura:*

{  
  "users": {
   
    "<id_aleatorio>": {
     
      "criado_em": "2025-06-13T15:07:05.459528",     // string no formato ISO (data/hora de criação)
      
      "nome": "Amanda",                              // string
      "email": "amanda@test.com",                    // string
      "genero": "Pop",                               // string (gênero musical)
      "musica_recomendada": {                        // objeto com info da música recomendada
        "titulo": "Musica",                          // string
        "artista": "Artista",                         // string
        "link": "https://www.deezer.com/track/...",  // string (URL da música)
        "preview": "https://...",                    // string (link para prévia)
        }
      }
  }
}

## Front react native:
- Link Snack: https://snack.expo.dev/@amandacaps/projeto-com-fastapi-13-6
***********************************************************************************************
