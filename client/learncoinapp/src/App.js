import logo from './logo.svg';
import './App.css';
import React from 'react';
import Box from '@material-ui/core/Box';
import TextField from '@material-ui/core/TextField';

function App() {
  return (
    <div className="App">
      <header className="App-header">
      <Box
      sx={{
        width: '30em',
        height: 200,
        backgroundColor: '#000A24',
        border: '4px solid #BCED09',
        borderRadius: '8px',
        // '&:hover': {
        //   backgroundColor: '#BCED09',
        //   opacity: [0.9, 0.8, 0.7],
        // },
      }
    }
    />
    <br></br>
    <Box
      component="img"
      sx={{
        width: '5.25em',
        height: '2em',
        backgroundColor: '#000A24',
        border: '4px solid #BCED09',
        borderRadius: '100px',
        '&:hover': {
          borderRadius: '20px',
        },
      }}
      src="https://i.imgur.com/lV5fq97.png"
    />
    <br></br>
    <Box
        component="img"
        sx={{
          height: 62,
          width: '100%',
        }}
        src="https://i.imgur.com/ADseBD8.png"
      />
      <br></br>
      <Box
      sx={{
        width: '7em',
        height: '3em',
        backgroundColor: '#000A24',
        border: '4px solid #BCED09',
        borderRadius: '8px',
        flexWrap: 'nowrap',
        // '&:hover': {
        //   backgroundColor: '#BCED09',
        //   opacity: [0.9, 0.8, 0.7],
        // },
      }
    }
    />
    <Box
      sx={{
        width: '7em',
        height: '3em',
        backgroundColor: '#000A24',
        border: '4px solid #BCED09',
        borderRadius: '8px',
        flexWrap: 'nowrap',
        // '&:hover': {
        //   backgroundColor: '#BCED09',
        //   opacity: [0.9, 0.8, 0.7],
        // },
      }
    }
    />
      </header>
    </div>
  );
}

export default App;
