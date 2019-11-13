import React, { createContext } from "react";

const initialState = {};

const CodeContext = createContext(initialState);

const CodeProvider = ({ children }: { children: any }) => {
  const test = {};

  const value = { test };

  return <CodeContext.Provider value={value}>{children}</CodeContext.Provider>;
};

export { CodeProvider, CodeContext };
