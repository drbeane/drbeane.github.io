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
      width: 1000px;
      height: 1000px;
      margin: 5px;
    }
  </style>

  <script async src="https://cdn.datacamp.com/dcl-react-dev.js.gz"></script>
</head>


  <div class="exercise">
    <div class="title">
      <h2>Example: np.where</h2>
    </div>
    <div data-datacamp-exercise data-lang="python" data-height="auto">
      <code data-type="pre-exercise-code"></code>
      <code data-type="sample-code">
        import numpy as np

        X = np.array(
          [[ 0.4,  1.2, -0.6],
           [ 1.6, -0.9,  0.5],
           [-0.4, -1.4,  1.7]]
        )

        Z = np.where(X < 0, 0, X)

        print(Z)
      </code>
      <code data-type="solution"></code>
      <code data-type="sct"></code>
      <!--<div data-type="hint">Just press 'Run'.</div>-->
    </div>
  </div>

  <div class="exercise">
    <div class="title">
      <h2>Example: np.where</h2>
    </div>
    <div data-datacamp-exercise data-lang="python" data-height="auto">
      <code data-type="pre-exercise-code"></code>
      <code data-type="sample-code">
        import numpy as np
        np.random.seed(1)

        prob = np.random.uniform(low=0, high=1, n=10)

        pred = np.where(p < 0.5, 'A', 'B')

        print('prob =', prob, '\n')
        print('pred =', pred)

      </code>
      <code data-type="solution"></code>
      <code data-type="sct"></code>
      <!--<div data-type="hint">Just press 'Run'.</div>-->
    </div>
  </div>
