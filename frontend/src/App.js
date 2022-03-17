import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Layout from './hocs/Layout';
import Category from './components/Category';
import Home from './components/Home';

const App = () => (
    <Layout>
        <Routes>
            <Route index element={<Home/>} />
            <Route path='/category/:slug' element={<Category/>} />
        </Routes>
    </Layout>
);

export default App;