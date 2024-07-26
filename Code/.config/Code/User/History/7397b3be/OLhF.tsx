import { useContext } from "react"
import { pathFindingContext } from "../context/PathfindingContext"

export const usePathfinding = () => {
    const context = useContext(pathFindingContext)

    if (!context) {
        throw new Error("usePathFinding must be used within a PathFindingProviding")
    }

    return context
}