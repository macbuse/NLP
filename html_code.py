html_wrapper = '''<head>
  <title>Bootstrap Example</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
  <style>
  /* Tooltip */
  .test + .tooltip > .tooltip-inner {
      background-color: #73AD21; 
      color: #FFFFFF; 
      border: 1px solid green; 
      padding: 15px;
      font-size: 20px;
  }
  /* Tooltip on top */
  .test + .tooltip.top > .tooltip-arrow {
      border-top: 5px solid green;
  }
  
  .test1 + .tooltip > .tooltip-inner {
      background-color: #FF9999; 
      color: #FFFFFF; 
      border: 1px solid black; 
      padding: 15px;
      font-size: 20px;
  }
  /* Tooltip on top */
  .test1 + .tooltip.top > .tooltip-arrow {
      border-top: 5px solid green;
  }

  </style>
</head>
<body>

<div class="container">
<br><br><br><br><br><br>
%s
</div>

<script>
$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip();   
});
</script>

</body>
</html>'''