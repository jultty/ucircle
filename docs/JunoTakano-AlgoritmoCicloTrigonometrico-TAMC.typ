#import "@local/skolar:0.2.0": *
#import "@preview/tablex:0.0.8": tablex, cellx, colspanx, rowspanx

#let meta = (
  title: [Algoritmo para recriar \ o Ciclo Trigonométrico],
  author: "Juno Takano",
  course: "Tópicos Avançados de Matemática para Computação",
  course_id: "TAMC",
  date: datetime.today().display("[day]/[month]/[year]"),
  flipped: true,
  margin_x: 2cm,
  margin_y: 2cm,
)

#let fig(path, caption) = {
  pad(y: 0em, [
    #figure(
      image(path, width: 100%),
      caption: caption
    )
  ])
}

#generate_document(properties: meta)[
  #fig("img/320.png", [Saída do algoritmo desenvolvido para a entrada `320`.])

  O presente trabalho e o código fonte associados permitem obter uma recriação do ciclo trigonométrico com representações visuais:

  1. Da função seno
  1. Da função cosseno
  1. Do ponto encontrado no ciclo trigonométrico dado um determinado ângulo
  1. Do seno encontrado dado um determinado ângulo
  1. Do cosseno encontrado dado um determinado ângulo
  1. Dos triângulos formados por estes três pontos
  1. Pela hipotenusa encontrada para estes três pontos

  #fig("img/120.png", [Saída do algoritmo desenvolvido para a entrada `120`.])

  O valor recebido em ângulos é convertido para um valor correspondente em radianos. Ambos os valores são exibidos na tela junto dos valores numéricos e gráficos para o cosseno, seno e ponto do ângulo no ciclo trigonométrico.

  Estas representações são exibidas sobre um plano cartesiano, com eixos $x$ e $y$ anotados com os respectivos valores em uma escala decimal de 1:1.

  #fig("img/79.png", [Saída do algoritmo desenvolvido para a entrada `79`.])

  O código fonte deste algoritmo foi entregue junto ao trabalho e também está disponível online em #link("https://github.com/jultty/ucircle").

]
