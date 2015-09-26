$(function () {
  // Grab the template script
  var source = $("#convo-template").html();

  // Compile the template
  var template = Handlebars.compile(source);

  var context={
    "question": "What is the best color?",
    "rating": "128",
    "user": [
      {"name": "Chuck", "stance": "I have always loved blue."},
      {"name": "Dave", "stance": "My favorite color is blood."}
    ],
    "message": [
      {"name": "Chuck", "time": "Tuesday, July 4th, 4:38PM", "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur a pretium ante, at ultricies mauris. Phasellus ac odio lobortis, dignissim augue sed, sagittis enim. Pellentesque vitae tincidunt urna. Ut consequat feugiat fermentum. Fusce quis mauris molestie, cursus dolor ac, rhoncus mauris. Pellentesque vulputate nunc et volutpat viverra. Aenean laoreet lacus ut diam lobortis ornare.Nulla mollis leo nulla, vitae consectetur ex volutpat ut. Fusce cursus, urna interdum ultricies porta, dui urna vehicula orci, at consectetur sapien ligula ultrices purus. Praesent nunc magna, gravida ut lectus in, mattis ultrices quam. Ut convallis nisl eu massa luctus, a cursus velit tempus. Proin imperdiet aliquet consectetur. Mauris placerat eu justo id tincidunt. Nam et nisl arcu.Cras eu tortor lacus. Donec neque libero, dictum ac lacus nec, finibus tempor metus. In nec nisl diam. Nullam ac ullamcorper nunc. Maecenas vestibulum pharetra blandit. Aliquam at elementum dui. Ut ac suscipit urna. Integer lectus nisi, pretium ut consequat a, sagittis et enim. Nullam maximus orci ac tincidunt blandit. Maecenas quam est, facilisis at mauris sed, suscipit congue mi. Aenean aliquam a ipsum non varius. Quisque ultrices enim lacus, in finibus elit interdum pharetra. Quisque vel ex tristique, laoreet dui in, tristique lectus. Morbi id augue malesuada, facilisis lectus nec, congue justo. Maecenas non eros ultrices, porta arcu semper, condimentum purus. Curabitur id tincidunt est."},
      {"name": "Dave", "time": "Tuesday, July 4th, 5:05PM", "content": "why"},
      {"name": "Chuck", "time": "Thursday, July 6th, 6:00PM", "content": "i hate you"}
    ]
  }

  // Add the compiled html to the page
  //$('.content-placeholder').html(template(context));
  $(document.body).append(template(context));
});
