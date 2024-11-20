// TODO: import useLocation from react-router-dom
import {useLocation} from 'react-router-dom';

function Search() {

  // TODO: create a variable to use the location hook
const location = useLocation();
const query = new URLSearchParams(location.search);
const q = query.get('q');
return <div>Search Query: {q}</div> 

console.log(query)
  // TODO: use URLSearchParams to get the query parameter from the URL

  // TODO: get the value of the query "q" parameter

  return (
    <div>
      <h1>Search Page</h1>
      {/* TODO: display the query parameter */}
      <h1>Search Results for: {q}</h1>
    </div>
  );
}

export default Search;
