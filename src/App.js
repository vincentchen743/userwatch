import './App.css';
import Typography from '@mui/material/Typography';
import TextField from '@mui/material/TextField';
import Box from '@mui/system/Box';
import Container from '@mui/material/Container';
import Button from '@mui/material/Button';
import React from 'react';
import { submitTypingProfile } from './Api';

function App() {
  const texts = [
    "Who washes the windows by Harold the fox.",
    "The quick brown fox washes the dishes and stares out Wendy's window.",
    "Humpdy Dumpty washes windows and jumps over the wall.",
    "Windows by the sea shore require regular washes to see out."
  ];
  const [randomText, setRandomText] = React.useState(texts[Math.floor(Math.random() * texts.length)]);
  const [disableBtn, setDisableBtn] = React.useState(true);
  const [name, setName] = React.useState('');
  const [typedText, setTypedText] = React.useState('');
  const [userTime, setUserTime] = React.useState([]);
  const [enteredText, setEnteredText] = React.useState([]);
  const [complete, setComplete] = React.useState(false);
  const [similar, setSimilar] = React.useState('');

  React.useEffect(() => {
    if (typedText.localeCompare(randomText) === 0 && name !== '') {
      setDisableBtn(false);
    } else {
      setDisableBtn(true);
    }
  }, [typedText]);

  const handleKeyDown = (e) => {
    const newTime = [...userTime];
    const newEnteredText = [...enteredText];
    newTime.push(new Date().getTime());
    newEnteredText.push(e.key);
    setUserTime(newTime);
    setEnteredText(newEnteredText);
  }

  const handleSubmit = async () => {
    setRandomText(texts[Math.floor(Math.random() * texts.length)]);
    const response = await submitTypingProfile(name, userTime, enteredText);
    setName('');
    setTypedText('');
    setUserTime('');
    setEnteredText('');
    setComplete(true);
    setSimilar(response.similar_user);
  }

  return (
    <Container maxWidth="sm" className="App">
      <Box>
        <Typography variant="h3" sx={{mb: 2}}>Typing Similarity Detector</Typography>
        <Typography variant="h5">Text to type:</Typography>
        <Box
          sx={{border: 1, padding: 2}}  
        >
          <Typography variant="subtitle1">{randomText}</Typography>
        </Box>
        <TextField 
          label="Name"
          variant="outlined"
          fullWidth
          onChange={(e) => setName(e.target.value)}
          value={name}
          sx={{
            my: 2
          }}
        />
        <TextField
          label="Enter text"
          multiline
          fullWidth
          minRows={4}
          variant="outlined"
          onChange={(e) => setTypedText(e.target.value)}
          onKeyDown={handleKeyDown}
          value={typedText}
          sx={{
            mb: 2
          }}
        />
        <Button
          variant="contained"
          disabled={disableBtn}
          onClick={handleSubmit}
          fullWidth
        >
          Submit
        </Button>
        {complete &&
          <Typography variant="subtitle1">
            Your typing was most similar to: {similar}
          </Typography>}
      </Box>
    </Container>
  );
}

export default App;
