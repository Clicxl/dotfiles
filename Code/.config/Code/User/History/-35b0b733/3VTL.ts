import { AlgorithmType } from "../utils/types";

interface PathFindingContextInterface {
    algorithm : AlgorithmType;
    setAlgorithm: (algorithum: AlgorithmType) => void;
    maze: MazeType;
}