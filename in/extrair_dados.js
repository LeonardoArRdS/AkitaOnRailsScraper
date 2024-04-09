//https://akitaonrails.com/
var posts = [];

for(var post of document.querySelectorAll(".posts")){
    var link = post.querySelector("a").href;
    var titulo = post.querySelector(".post-title").innerText;
    var info = post.querySelector(".informations").childNodes[0].textContent.trim();
    var tags = [];

    post.querySelectorAll(".tags a").forEach(function(tagElem) {
        var tagLink = tagElem.href;
        var tagText = tagElem.innerText;

        tags.push({
            "tagLink" : tagLink,
            "tagText" : tagText
        });

    });

    posts.push({
        "link" : link,
        "titulo" : titulo,
        "info" : info,
        "tags" : tags
    });
}

console.log(JSON.stringify(posts));