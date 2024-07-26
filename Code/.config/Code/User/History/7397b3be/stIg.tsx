import { useContext } from "react"
import { pathFindingContext } from "../context/PathFindingContext"
import { pathFindingContextTy}

export const usePathFinding = () => {
    const context = useContext(pathFindingContext)

    if (!context) {
        throw new Error("usePathFinding must be used within a PathFindingProviding")
    }

    return context
}