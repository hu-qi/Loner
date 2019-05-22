留言板
===

Hello World！

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/gitalk@1/dist/gitalk.css">
<script src="https://cdn.jsdelivr.net/npm/gitalk@1/dist/gitalk.min.js"></script>
<div id="gitalk-container"></div>
<script>
  var gitalk = new Gitalk({
    "clientID": "9386190044f0a54a0e00",
    "clientSecret": "bc4eb0013e6e2c496b1978724b93b939cb248992",
    "repo": "Loner",
    "owner": "hu-qi",
    "admin": ["hu-qi"],
    "id": location.pathname,      
    "distractionFreeMode": false  
  });
  gitalk.render("gitalk-container");
</script>