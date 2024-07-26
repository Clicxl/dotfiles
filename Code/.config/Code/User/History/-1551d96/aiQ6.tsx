import { useContext } from "react"
import { PathfindingContext } from "../context/PathfindingContext"

export const usePathfinding = () => {
    const context = useContext(Tile)

    if (!context) {
        throw new Error("usePathFinding must be used within a PathFindingProviding")
    }

    return context
}