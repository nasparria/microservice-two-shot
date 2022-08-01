import { BrowserRouter, Routes, Route } from 'react-router-dom';
import MainPage from './MainPage';
import Nav from './Nav';
import AllShoes from './ShoesList';
import NewShoesForm from './NewShoesForm'

function App() {
  return (
    <BrowserRouter>
      <Nav />
      <div className="container">
        <Routes>
          <Route path="/" element={<MainPage />} />
          <Route path="/shoes" element={<AllShoes />} />
          <Route path="/shoes/create" element={<NewShoesForm />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
