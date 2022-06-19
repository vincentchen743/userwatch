export const url = 'http://localhost:8080';

export async function submitTypingProfile (name, userTime, enteredText) {
  const response = await fetch(`${url}/typingprofiles`, {
    method: 'POST',
    headers: {
      'Content-type': 'application/json',
    },
    body: JSON.stringify({
      name,
      userTime,
      enteredText
    })
  });
  if (response.ok) {
    const data = await response.json();
    return data;
  }
  return null;
}