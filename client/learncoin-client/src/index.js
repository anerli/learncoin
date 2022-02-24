import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Routes, Route } from "react-router-dom";

import './index.css';
import Blockchain from './Pages/Blockchain';
import Homepage from "./Pages/Homepage";
import Login from "./Pages/Login";
import Mining from "./Pages/Mining";
import Signup from "./Pages/Signup";

export default function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Login />}>
                    <Route path="homepage" element={<Homepage />} />
                    <Route path="signup" element={<Signup />} />
                    <Route path="mining" element={<Mining />} />
                    <Route path="blockchain" element={<Blockchain />} />
                </Route>
            </Routes>
        </BrowserRouter>
    );
}

ReactDOM.render(<App />, document.getElementById('root'));
