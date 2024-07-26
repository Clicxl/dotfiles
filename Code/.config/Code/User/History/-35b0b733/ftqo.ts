import { AlgorithmType, MazeType, GridType } from "../utils/types";

interface PathFindingContextInterface {
  algorithm: AlgorithmType;
  setAlgorithm: (algorithum: AlgorithmType) => void;
  maze: MazeType;
  setMaze: (maze: MazeType) => void;
  grid: GridType;
  setGrids: (grid: GridType) => void;
  isGraphVisualized: boolean;
  setIsGraphVisualized: (isGraphVisualized: boolean) => void;
}

export const pathFindingContext:PathFindingContextInterface