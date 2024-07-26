import { useContext } from "react"
import { PathfindingContext } from "../context/PathFindingContext"

export const usePathFinding = () => {
    const context = useContext(pathFindingContext)

    if (!context) {
        throw new Error("usePathFinding must be used within a PathFindingProviding")
    }

    return context;
}
