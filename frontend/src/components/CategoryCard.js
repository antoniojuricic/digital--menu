import React from 'react'

function CategoryCard(props) {
  return (
    <div className="category-card">
       <div className="category-title">
            { props.title }
        </div>
    </div>
  )
}

export default CategoryCard
