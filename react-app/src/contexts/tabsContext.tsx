import React, { createContext, useState } from "react";

const initialState: any = 0;

const TabsContext = createContext(initialState);

const TabsProvider = ({ children }: { children: React.ReactNode }) => {
  const [value, setValue] = useState(2);

  const handleChangeIndex = (index: any) => {
    setValue(index);
  };

  const handleChange = (event: React.ChangeEvent<{}>, newValue: number) => {
    setValue(newValue);
  };
  return (
    <TabsContext.Provider
      value={{
        value,
        handleChange,
        handleChangeIndex
      }}
    >
      {children}
    </TabsContext.Provider>
  );
};

export { TabsProvider, TabsContext };
