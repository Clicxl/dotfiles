import { useContext } from "react";
import { pathFindingContext } from "../context/PathfindingContext";

export const usePathfinding = () => {
  const context = useContext(pathFindingContext);

  if (!context) {
    throw new Error("usePathfinding must be used within a PathfindingProvider");
  }

  return context;
};