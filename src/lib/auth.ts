export const getToken = () => {
  if (typeof window === 'undefined') return null;
  return localStorage.getItem('authToken');
};

export const setToken = (token: string) => {
  localStorage.setItem('authToken', token);
};

export const removeToken = () => {
  localStorage.removeItem('authToken');
};

export const getUser = () => {
  if (typeof window === 'undefined') return null;
  const user = localStorage.getItem('authUser');
  return user ? JSON.parse(user) : null;
};

export const setUser = (user: any) => {
  localStorage.setItem('authUser', JSON.stringify(user));
};

export const removeUser = () => {
  localStorage.removeItem('authUser');
};

export const isAuthenticated = () => {
  return !!getToken();
};
