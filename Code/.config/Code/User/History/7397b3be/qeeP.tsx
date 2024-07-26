import { useContext } from "react";

export const usePathfinding = () => {
  const context = useContext(PathF);

  if (!context) {
    throw new Error("usePathfinding must be used within a PathfindingProvider");
  }

  return context;
};