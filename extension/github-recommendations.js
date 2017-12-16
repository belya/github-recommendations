$(function() {
  $(".dashboard-sidebar").prepend('<div class="recommended-repos boxed-group flush js-repos-container" data-pjax-container="" role="navigation"><h3>Recommended repositories</h3><div class="boxed-group-inner"><ul class="mini-repo-list"></ul></div></div>')
  var repositories = ["lol/lol"]
  repositories.map(repo => {
    $(".recommended-repos .mini-repo-list").append('<li class="public source no-description"><a href="' + repo + '" class="mini-repo-list-item css-truncate"><svg aria-label="Repository" class="octicon octicon-repo repo-icon" height="16" role="img" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"></path></svg><span class="repo-and-owner css-truncate-target"><span class="owner css-truncate-target" title="Historicteam">' + repo.split("/")[0] + '</span>/<span class="repo">' + repo.split("/")[1] + '</span></span></a></li>')
  })
})