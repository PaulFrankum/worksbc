const { getUserRepos } = require("./github");

// TODO: Enter your GitHub username
const gitHubUser = "PaulFrankum";

getUserRepos(gitHubUser).then((repos) => {
  console.log(repos);
});
