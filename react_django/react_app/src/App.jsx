
import './App.css'
import DeleteFile from './Components/DeleteFile';
import Records from './Components/Records';
import Upload from './Components/Upload';
import { BrowserRouter as Router,Routes,Route,Link } from 'react-router-dom';
import Video from './Components/Video';


function App() {

  return (
    <>
      <Router>
        <nav>
          <button><Link to="/">Home</Link></button>
          <button><Link to="/upload">Upload</Link></button>
        </nav>
        <Routes>
          <Route path="/" element={<Records/>}/>
          <Route path="/upload" element={<Upload/>}/>
          <Route path="/deletefile/:id/" element={<DeleteFile/>}/>
          <Route path="/video/:id/" element={<Video/>}/>
        </Routes>
      </Router>
    </>
  )
}

export default App
