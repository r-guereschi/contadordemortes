Contador de Mortes para Livestreams

Este é um contador de mortes desenvolvido em Python com interface gráfica usando a biblioteca Tkinter. Ele foi projetado para ser usado como um contador de mortes em transmissões ao vivo, como no contexto de jogos de vídeo, onde os espectadores podem acompanhar o número de mortes ocorridas durante a gameplay.

Linguagem Utilizada: Python

Bibliotecas Utilizadas:

Tkinter: Para a criação da interface gráfica.
Pynput: Para capturar os eventos de teclado.
Threading: Para criar processos separados para controlar a animação de transição do contador.

Funcionalidades:

Contagem de Mortes: O programa permite que o usuário conte o número de mortes ocorridas em um jogo durante uma transmissão ao vivo. Os espectadores podem ver o contador em tempo real enquanto assistem à transmissão.
Interação por Teclado: O programa responde aos eventos de teclado, permitindo que o usuário adicione uma morte pressionando a tecla Enter, subtraia uma morte pressionando a tecla Backspace e redefina o contador para zero pressionando a tecla Delete.

Uso:

Durante a transmissão ao vivo, use o programa para contar as mortes no jogo pressionando as teclas Enter (adicionar morte), Backspace (subtrair morte) ou Delete (redefinir contador).
O contador será exibido na tela da transmissão, permitindo que os espectadores acompanhem o número de mortes em tempo real.
Use o recurso de Chroma Key do OBS para incorporar o contador à sobreposição da transmissão. Configure o fundo verde do contador para que ele possa ser removido facilmente usando o Chroma Key no OBS.
Este programa foi projetado para oferecer uma solução simples e eficaz para contar mortes durante transmissões ao vivo, tornando a experiência mais interativa e envolvente para os espectadores.
