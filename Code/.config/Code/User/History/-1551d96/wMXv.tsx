import { useContext } from "react"
import { PathfindingContext } from "../context/PathfindingContext"
import { TileContext } from "../context/TileContext"

export const usePathfinding = () => {
    const context = useContext(TileContext)

    if (!context) {
        throw new Error("usePathFinding must be used within a PathFindingProviding")
    }

    return context
}