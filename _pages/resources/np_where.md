---
layout: archive
permalink: /resources/np_where
title: "Tutorial on np.where"
author_profile: true
header:
  image: "/images/druidarch.jpg"
---

+ [DataCamp](example.html)



<head>
  <meta charset="utf-8" />
  <title>DataCamp Light | Standalone example</title>
  <link rel='shortcut icon' type='image/x-icon' href='https://www.datacamp.com/assets/favicon.ico'/>
  <style>
    .exercise {
      width: 1000px;
      margin: 5px;
    }
  </style>

  <script async src="https://cdn.datacamp.com/dcl-react-dev.js.gz"></script>
</head>


  <div class="exercise">
    <div class="title">
      <h2>Example: np.where</h2>
    </div>
    <div data-datacamp-exercise data-lang="python" data-height="400px">
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

+ Example 2: Determining Predicted Classes

We can us `np.where` to blah blah blah.

  <div class="exercise">
    <div class="title">
      <h2>Example: np.where</h2>
    </div>
    <div data-datacamp-exercise data-lang="python" data-height="400px">
      <code data-type="pre-exercise-code"></code>
      <code data-type="sample-code">
        import numpy as np
        np.set_printoptions(suppress=True, precision=2)
        np.random.seed(1)

        prob = np.random.uniform(low=0, high=1, size=8)

        pred = np.where(prob < 0.5, 'A', 'B')

        print('prob =', prob, '\n')
        print('pred =', pred)

      </code>
      <code data-type="solution"></code>
      <code data-type="sct"></code>
      <!--<div data-type="hint">Just press 'Run'.</div>-->
    </div>
  </div>
