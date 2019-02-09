---
layout: archive
permalink: /classes/
title: "My Classes"
author_profile: true
header:
  image: "/images/iceland.jpg"
---
These are some classes.

MTH 34500

DSCI 11000

+ [DataCamp](example.html)
+ [lesson1](lesson01.html)
+ [lesson2](lesson02.html)
+ [lesson3](lesson03.Rmd)
+ [lesson4](lesson04.ipynb)

<head>
  <meta charset="utf-8" />
  <title>DataCamp Light | Standalone example</title>
  <link rel='shortcut icon' type='image/x-icon' href='https://www.datacamp.com/assets/favicon.ico'/>
  <style>
    .exercise {
      margin: 50px;
    }
  </style>

  <script async src="https://cdn.datacamp.com/dcl-react-dev.js.gz"></script>
</head>


  <div class="exercise">

    <div class="title">
      <h2>This is an python exercise with a plot</h2>
    </div>

    <div data-datacamp-exercise data-lang="python" data-height="auto">
      <code data-type="pre-exercise-code"></code>
      <code data-type="sample-code">
        import numpy as np
        import matplotlib.pyplot as plt

        x = np.arange(0, 5, 0.1);
        y = np.sin(x)
        plt.plot(x, y)
        plt.show()
      </code>
      <code data-type="solution"></code>
      <code data-type="sct"></code>
      <!--<div data-type="hint">Just press 'Run'.</div>-->
    </div>
  </div>